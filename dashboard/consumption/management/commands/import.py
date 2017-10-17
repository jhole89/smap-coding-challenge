from django.core.management.base import BaseCommand
from consumption.models.consumption import Consumption
from consumption.models.user import User
from dashboard import settings
from datetime import datetime
import glob
import csv
import os


class Command(BaseCommand):
    help = 'import data'

    def handle(self, *args, **options):

        data_dir = os.path.join(
            os.path.dirname(settings.BASE_DIR),
            'data'
        )

        user_path = os.path.join(
            data_dir,
            'user_data.csv'
        )

        with open(user_path, 'r') as user_data:
            reader = csv.DictReader(user_data, delimiter=',')

            for record in reader:
                user = User()
                user.id = int(record['id'])
                user.area = record['area']
                user.tariff = record['tariff']
                user.save()

        consumption_path = os.path.join(
            data_dir,
            'consumption',
            '*.csv'
        )

        consumption_files = glob.glob(consumption_path)

        for con_file in consumption_files:

            with open(con_file, 'r') as con_data:
                reader = csv.DictReader(con_data, delimiter=',')

                for record in reader:
                    usage = Consumption()
                    usage.timestamp = datetime.strptime(record['datetime'], '%Y-%m-%d %H:%M:%S')
                    usage.consumption = float(record['consumption'])
                    usage.save()
