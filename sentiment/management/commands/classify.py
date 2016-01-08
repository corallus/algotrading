from django.core.management.base import BaseCommand
from news_retrieval.utils import fetch as news_fetch
from stock_retrieval.utils import fetch as stock_fetch
from sentiment.utils import train, classify


class Command(BaseCommand):
    def handle(self, *args, **options):
        stock_fetch()
        news_fetch()
        classifier = train()
        classify(classifier)
