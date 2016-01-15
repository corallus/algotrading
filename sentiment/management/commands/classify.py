from django.core.management.base import BaseCommand
import time
from openpyxl import Workbook
import datetime
from django.conf import settings

from credibility.models import calculate_credibility
from sentiment.utils import train, classify, predict


class Command(BaseCommand):
    def handle(self, *args, **options):
        wb = Workbook()
        ws = wb.active  # grab the active worksheet
        while True:
            accuracies = [datetime.datetime.now()]
            classifier, accuracy = train()
            # check whether there is training data to create a classifier
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
            wb.save(settings.FILE)
            time.sleep(50)
