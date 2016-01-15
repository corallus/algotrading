from django.core.management.base import BaseCommand
import time
from openpyxl import Workbook
import datetime

from credibility.models import calculate_credibility
from social_retrieval.utils import fetch as fetch_tweets
from news_retrieval.utils import fetch as fetch_news
from sentiment.utils import train, classify, predict


class Command(BaseCommand):
    def handle(self, *args, **options):
        wb = Workbook()
        ws = wb.active  # grab the active worksheet
        while (True):
            news_fetched = fetch_news()
            tweets_fetched = fetch_tweets()
            if news_fetched or tweets_fetched:
                print('berichten gevonden')
                accuracies = [datetime.datetime.now()]
                classifier, accuracy = train()
                # check whether there was training data to create a classifier
                if classifier:
                    print('accuracy: %s' % accuracy)
                    accuracies.append(accuracy)
                    classifier.show_most_informative_features()
                    classify(classifier)  # classify unknown documents
                    calculate_credibility()
                    predict()
                else:
                    accuracies.append('')
                ws.append(accuracies)
            wb.save('/home/vincent/PycharmProjects/algotrading/export.xls')
            time.sleep(50)
