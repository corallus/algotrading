from django.core.management.base import BaseCommand
from social_retrieval.utils import fetch as fetch_tweets
from news_retrieval.utils import fetch as fetch_news
from sentiment.utils import train, classify
import time


minutes_after = [0, 5, 20, 40, 60, 100, 160, 260, 420, 680]


class Command(BaseCommand):
    def handle(self, *args, **options):
        while(True):
            news_fetched = fetch_news()
            tweets_fetched = fetch_tweets()
            if news_fetched or tweets_fetched:
                for minutes_after_article in minutes_after:
                    classifier = train(minutes_after_article)
                    # check whether there was training data to create a classifier
                    if classifier:
                        classifier.show_most_informative_features()
                        classify(classifier)  # classify unknown documents
            time.sleep(50)