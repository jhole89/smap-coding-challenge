# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


class User(models.Model):
    """
    The User class model with attributes:

        :id (int) integer ID field and primary key
        :area (str) string area field (a1|a2)
        :tariff (str) string tarrif field (t1|t2|t3)

    :return: None
    """

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
    """
    The Consumption class model with attributes:

        :user_id (model.User object) instance of User model and foreign key
        :timestamp (str) string datetime field
        :consumption (float) energy consumption used within timestamp

    :return: None
    """

    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField()
    consumption = models.FloatField()

    @classmethod
    def get_total(cls, user):
        """
        Get total consumption given a User

        :param user: (model.User object) an instance of User class
        :return: (float) total User consumption
        """

        user_consumptions = Consumption.objects.filter(user_id=user)

        total_consumptions = 0.0

        for consumption_record in user_consumptions:
            total_consumptions += consumption_record.consumption

        return total_consumptions

    @classmethod
    def get_average(cls, user):
        """
        Get average (mean) consumption given a User

        :param user: (model.User object) an instance of User class
        :return: (float) average User consumption
        """

        user_consumptions = Consumption.objects.filter(user_id=user)

        consumptions = []

        for consumption_record in user_consumptions:
            consumptions.append(consumption_record.consumption)

        if consumptions:
            avg_consumption = sum(consumptions)/float(len(consumptions))
        else:
            avg_consumption = 0.0

        return avg_consumption
