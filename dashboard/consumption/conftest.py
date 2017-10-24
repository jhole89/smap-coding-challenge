import os
import django
from django.conf import settings
import pytest
from datetime import datetime

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dashboard.settings')


def pytest_configure():
    settings.DEBUG = False
    django.setup()


@pytest.fixture(scope='module')
def testing_user():
    from consumption.models import User
    return User(id=1000, area='a1', tariff='t1')


@pytest.fixture(scope='module')
def consumption_record_1(testing_user):
    from consumption.models import Consumption
    return Consumption(
        user_id=testing_user,
        timestamp=datetime(
            year=2017, month=6, day=1, hour=14, minute=30, second=45),
        consumption=1250.75
    )


@pytest.fixture(scope='module')
def consumption_record_2(testing_user):
    from consumption.models import Consumption
    return Consumption(
        user_id=testing_user,
        timestamp=datetime(
            year=2017, month=6, day=2, hour=14, minute=30, second=45),
        consumption=1750.25
    )

