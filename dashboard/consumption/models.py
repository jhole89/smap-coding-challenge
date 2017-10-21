# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


class User(models.Model):

    AREA = (
        ('a1', 'area1'),
        ('a2', 'area2'),
    )

    TARIFF = (
        ('t1', 'tariff1'),
        ('t2', 'tariff2'),
        ('t3', 'tariff3'),
    )

    id = models.IntegerField(primary_key=True)
    area = models.CharField(max_length=2, choices=AREA)
    tariff = models.CharField(max_length=2, choices=TARIFF)


class Consumption(models.Model):

    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField()
    consumption = models.FloatField()

    def get_total(self, user):

        user_consumptions = Consumption.objects.filter(user_id=user)

        total_consumptions = 0.0

        for consumption_record in user_consumptions:
            total_consumptions += consumption_record.consumption

        return total_consumptions

    def get_average(self, user):

        user_consumptions = Consumption.objects.filter(user_id=user)

        avg_consumption = 0.0

        for record_count, consumption_record in enumerate(user_consumptions):
            avg_consumption += consumption_record.consumption

        avg_consumption = avg_consumption/float(record_count)

        return avg_consumption
