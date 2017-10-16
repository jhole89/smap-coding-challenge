# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from user import User


class Consumption(models.Model):

    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField()
    consumption = models.FloatField()
