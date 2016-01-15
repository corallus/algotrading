from django.core.management.base import BaseCommand
import time

from social_retrieval.utils import fetch as fetch_tweets
from news_retrieval.utils import fetch as fetch_news


class Command(BaseCommand):
    def handle(self, *args, **options):
        while True:
            fetch_news()
            fetch_tweets()
            time.sleep(50)
