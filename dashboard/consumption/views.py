# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from models import Consumption
from models import User

# Create your views here.


def summary(request):

    all_users = User.objects.all().values('id', 'area', 'tariff')
    user_data = []

    for user in all_users:

        user_data.append({
            'id': user.id,
            'total_consumption': Consumption.get_total(user),
            'avg_consumption': Consumption.get_average(user),
        })

    context = {
        'data': user_data,
    }
    return render(request, 'consumption/summary.html', context)


def detail(request):
    context = {
    }
    return render(request, 'consumption/detail.html', context)
