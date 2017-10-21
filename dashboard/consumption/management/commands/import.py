from django.core.management.base import BaseCommand
from consumption.models import Consumption, User
from dashboard import settings
from datetime import datetime
import logging
import glob
import csv
import os


class Command(BaseCommand):
    help = 'import data'

    def handle(self, *args, **options):

        stdlogger = logging.getLogger(__name__)

        data_dir = os.path.join(
            os.path.dirname(settings.BASE_DIR),
            'data'
        )

        user_path = os.path.join(
            data_dir,
            'user_data.csv'
        )

        stdlogger.info("Reading file: {}".format(user_path))

        with open(user_path, 'r') as user_data:
            reader = csv.DictReader(user_data, delimiter=',')

            for u_counter, record in enumerate(reader):
                user = User()
                user.id = int(record['id'])
                user.area = record['area']
                user.tariff = record['tariff']

                stdlogger.debug(
                    "Saving User object: Id: {}, Area: {}, Tariff: {}".format(
                        user.id, user.area, user.tariff))
                user.save()

        stdlogger.info("{} User records saved to database".format(u_counter))

        consumption_path = os.path.join(
            data_dir,
            'consumption',
            '*.csv'
        )

        consumption_files = glob.glob(consumption_path)

        for con_file in consumption_files:

            stdlogger.info("Reading file: {}".format(con_file))

            with open(con_file, 'r') as con_data:
                reader = csv.DictReader(con_data, delimiter=',')

                for c_counter, record in enumerate(reader):

                    usage = Consumption()

                    usage.user_id = User.objects.get(
                        id=int(os.path.split(con_file)[-1].rstrip('.csv')))
                    usage.timestamp = datetime.strptime(
                        record['datetime'], '%Y-%m-%d %H:%M:%S')
                    usage.consumption = float(record['consumption'])

                    stdlogger.debug(
                        "Saving Consumption object: "
                        "Id: {}, Area: {}, Tariff: {}".format(
                            usage.user_id, usage.timestamp, usage.consumption))
                    usage.save()

            stdlogger.info(
                "{} Consumption records saved to database".format(c_counter))
