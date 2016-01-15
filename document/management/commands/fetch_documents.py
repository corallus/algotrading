from django.core.management.base import BaseCommand
from social_retrieval.utils import fetch as fetch_tweets
from news_retrieval.utils import fetch as fetch_news
from sentiment.utils import train, classify
import time
from openpyxl import Workbook
import datetime

minutes_after = [0, 5, 15, 40, 80, 120, 200, 320, 520]


class Command(BaseCommand):
    def handle(self, *args, **options):
        wb = Workbook()
        ws = wb.active  # grab the active worksheet
        while(True):
            news_fetched = fetch_news()
            tweets_fetched = fetch_tweets()
            if news_fetched or tweets_fetched:
                accuracies = []
                accuracies.append(datetime.datetime.now())
                for minutes_after_article in minutes_after:
                    classifier, accuracy = train(minutes_after_article)
                    # check whether there was training data to create a classifier
                    if classifier:
                        accuracies.append(accuracy)
                        classifier.show_most_informative_features()
                        classify(classifier)  # classify unknown documents
                    else:
                        accuracies.append('')
                ws.append(accuracies)
            wb.save('/home/vincent/PycharmProjects/algotrading/export.xls')
            time.sleep(50)
