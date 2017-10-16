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
