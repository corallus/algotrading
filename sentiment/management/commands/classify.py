from django.core.management.base import BaseCommand
import time
from openpyxl import Workbook
import datetime
from django.conf import settings

from credibility.models import calculate_credibility
from sentiment.utils import train, classify, predict


class Command(BaseCommand):
    def handle(self, *args, **options):
        while True:
            accuracies = [datetime.datetime.now()]
            classifier, accuracy = train()
            # check whether there is training data to create a classifier
            if classifier:
                classifier.show_most_informative_features()
                classify(classifier)  # classify unknown documents
                calculate_credibility()
                prediction = predict()

                for share in prediction:
                    if prediction[share] > 0:
                        print('%s will go up (score: %s)' % (share, prediction[share]))
                    elif prediction[share] < 0:
                        print('%s will drop (score: %s)' % (share, prediction[share]))
                    else:
                        print('%s will remain the same (score: %s)' % (share, prediction[share]))
                print("\a")
            time.sleep(50)
