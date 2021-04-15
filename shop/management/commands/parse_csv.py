import csv
from pathlib import Path

from django.core.management import BaseCommand

from shop.models import Goods


class Command(BaseCommand):
    help = 'Load data from csv'

    def handle(self, *args, **options):

        # drop the data from the table so that if we rerun the file, we don't repeat values
        Goods.objects.all().delete()

        print("tables dropped successfully")
        # create table again

        # open the file to read it into the database
        base_dir = Path(__file__).resolve().parent.parent.parent.parent

        with open(str(base_dir) + '/shop/management/commands/SalesData.csv', newline='') as f:
            reader = csv.reader(f, delimiter=",")
            next(reader)  # skip the header line
            for row in reader:
                print(row)
                try:
                    Goods.objects.create(g_name=row[2], g_price=row[3])
                except Exception as e:
                    print("incomplete data row")
        print("data parsed successfully")
