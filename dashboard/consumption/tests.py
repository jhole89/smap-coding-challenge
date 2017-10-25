# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime
from models import Consumption
from models import User
import pytest


@pytest.mark.django_db
def test_save_user():
    """
    unittest for models.User creation and save

    :return: None
    """

    test_id = 1000
    test_area = 'a1'
    test_tariff = 't1'

    user = User(id=test_id, area=test_area, tariff=test_tariff)
    user.save()

    assert user.id == test_id
    assert user.area == test_area
    assert user.tariff == test_tariff


@pytest.mark.django_db
def test_save_consumption(testing_user):
    """
    unittest for model.Consumption creation and save

    :param (models.User object) testing_user: an instance of the User class
    :return: None
    """

    test_id = testing_user
    test_timestamp = datetime(
        year=2017, month=1, day=2, hour=3, minute=4, second=5)
    test_consumption = 101.11

    usage = Consumption(
        user_id=test_id, timestamp=test_timestamp, consumption=test_consumption
    )
    usage.save()

    assert usage.user_id == test_id
    assert usage.timestamp == test_timestamp
    assert usage.consumption == test_consumption


@pytest.mark.django_db
def test_get_total(testing_user, consumption_record_1, consumption_record_2):
    """
    unittest for calculation of total consumption per User

    :param (models.User object) testing_user: an instance of the User class
    :param (models.Consumption object) consumption_record_1: an instance of the Consumption class
    :param (models.Consumption object) consumption_record_2: an instance of the Consumption class
    :return: None
    """

    testing_user.save()
    consumption_record_1.save()
    consumption_record_2.save()

    total_user_consumption = Consumption.get_total(testing_user)

    assert total_user_consumption == 3001.0


@pytest.mark.django_db
def test_get_avg(testing_user, consumption_record_1, consumption_record_2):
    """
    unittest for calculation of average consumption per User

    :param (models.User object) testing_user: an instance of the User class
    :param (models.Consumption object) consumption_record_1: an instance of the Consumption class
    :param (models.Consumption object) consumption_record_2: an instance of the Consumption class
    :return: None
    """

    testing_user.save()
    consumption_record_1.save()
    consumption_record_2.save()

    avg_user_consumption = Consumption.get_average(testing_user)

    assert avg_user_consumption == 1500.5
