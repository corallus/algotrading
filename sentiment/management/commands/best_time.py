from django.core.management.base import BaseCommand
from openpyxl import Workbook
from django.conf import settings
from datetime import timedelta, datetime
from nltk.classify import NaiveBayesClassifier
from nltk.sentiment.util import *
from sentiment.utils import predict, get_nltktext, word_feats
from document.models import Document
from stock_retrieval.models import ShareValue


class Command(BaseCommand):
    def handle(self, *args, **options):
        wb = Workbook()
        ws = wb.active
        ws.title = 'first sheet'

        for time in range(1, 350, 5):
            # reset data
            Document.objects.update(sentiment=None, predicted_sentiment=None)

            relevant_docs = Document.objects.filter(published__gte=ShareValue.objects.first().time,
                                                    published__lte=ShareValue.objects.last().time - timedelta(
                                                        minutes=time), similar__isnull=True)

            for document in relevant_docs:

                sharevalue_before = ShareValue.objects.filter(share=document.share, time__lte=document.published,
                                                              time__gte=document.published - timedelta(
                                                                  minutes=5)).last()

                # first share value in the interval [d.published + time, d.published + time * 2]
                sharevalue_after = ShareValue.objects.filter(share=document.share,
                                                             time__gte=document.published + timedelta(minutes=time),
                                                             time__lte=document.published + timedelta(
                                                                 minutes=time * 2)).first()
                if sharevalue_after and sharevalue_before:
                    price_before = sharevalue_before.price
                    price_after = sharevalue_after.price
                    if price_after > price_before:
                        impact = 'pos'
                    elif price_before > price_after:
                        impact = 'neg'
                    else:
                        impact = 'neu'
                    document.sentiment = impact
                    document.save()

            known_feats = []
            for doc in Document.objects.filter(sentiment__isnull=False, similar__isnull=True):
                text = get_nltktext(doc.text)
                known_feats.append((word_feats(text), doc.sentiment))
            if known_feats:
                known_data_count = len(known_feats)

                # 2/3 training data
                num_training_data = int(round(2 * known_data_count / 3))
                training_feats = known_feats[:num_training_data]
                classifier = NaiveBayesClassifier.train(training_feats)
                classifier.show_most_informative_features()

                # 1/3 test_data
                num_testing_data = int(round(known_data_count / 3))
                testing_feats = known_feats[::-1][:num_testing_data]
                accuracy = nltk.classify.util.accuracy(classifier, testing_feats)

                ws.append([time, accuracy])
                wb.save(settings.FILE)
