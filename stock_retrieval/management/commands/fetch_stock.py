from django.core.management.base import BaseCommand
from stock_retrieval.utils import fetch as fetch_stock
import time
from datetime import datetime


class Command(BaseCommand):
    def handle(self, *args, **options):
        while True:
            fetch_stock()
            print(datetime.now())
            time.sleep(60)
