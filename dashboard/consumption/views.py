# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from models import Consumption
from models import User
import json


def summary(request):
    """
    Summary view to parse user-aggregated data to frontend

    :param request: GET request
    :return: rendered JSON object
    """

    all_users = User.objects.all()
    user_data = []

    for user in all_users:

        user_data.append({
            'id': user.id,
            'area': user.area,
            'tariff': user.tariff,
            'total_consumption': Consumption.get_total(user),
            'avg_consumption': int(Consumption.get_average(user)),
        })

    context = {
        'data': json.dumps(user_data),
    }
    return render(request, 'consumption/summary.html', context)


def detail(request):
    context = {
    }
    return render(request, 'consumption/detail.html', context)
