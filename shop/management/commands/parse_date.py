import csv
from pathlib import Path

from django.core.management import BaseCommand
from django.utils import timezone

from shop.models import productionDate


class Command(BaseCommand):
    help = 'Load data from csv'

    def handle(self, *args, **options):

        # drop the data from the table so that if we rerun the file, we don't repeat values
        productionDate.objects.all().delete()

        print("tables dropped successfully")
        # create table again

        # open the file to read it into the database
        base_dir = Path(__file__).resolve().parent.parent.parent.parent

        with open(str(base_dir) + '/shop/management/commands/SalesData.csv', newline='') as f:
            reader = csv.reader(f, delimiter=",")
            next(reader)  # skip the header line
            for row in reader:
                print(row)
                print(row[4], row[0])
                try:
                    productionDate.objects.create(production_date=row[4], good_id=row[0])
                except Exception as e:
                    print("incomplete data row")
        print("data parsed successfully")
