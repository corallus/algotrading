from django.core.management.base import BaseCommand
from social_retrieval.utils import fetch as fetch_tweets
from news_retrieval.utils import fetch as fetch_news
from sentiment.utils import train, classify
import time


class Command(BaseCommand):
    def handle(self, *args, **options):
        while(True):
            news_fetched = fetch_news()
            tweets_fetched = fetch_tweets()
            if news_fetched or tweets_fetched:
                classifier = train()
                # check whether there was training data to create a classifier
                if classifier:
                    classify(classifier) # classify unknown documents
            time.sleep(10)