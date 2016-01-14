from django.core.management.base import BaseCommand
from stock_retrieval.utils import fetch as fetch_stock
from news_retrieval.utils import fetch as fetch_news
from sentiment.utils import train, classify
import time


class Command(BaseCommand):
    def handle(self, *args, **options):
        while(True):
            fetch_stock()
            fetch_news()
            classifier = train()
            if classifier:
                classify(classifier)
            time.sleep(10)