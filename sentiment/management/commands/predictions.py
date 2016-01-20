from django.core.management.base import BaseCommand
from openpyxl import Workbook
from django.conf import settings
from datetime import timedelta
from nltk.classify import NaiveBayesClassifier
from credibility.models import calculate_credibility
from sentiment.utils import predict, get_nltktext, word_feats
from document.models import Document
from stock_retrieval.models import ShareValue


class Command(BaseCommand):
    def handle(self, *args, **options):
        wb = Workbook()
        ws = wb.active
        ws.title = 'first sheet'

        time = 21

        # reset data
        Document.objects.update(sentiment=None, predicted_sentiment=None)
        relevant_docs = Document.objects.filter(published__gte=ShareValue.objects.first().time,
                                                published__lte=ShareValue.objects.last().time - timedelta(
                                                    minutes=time))

        for d in relevant_docs:
            # last sharevalue in interval [d.published - time, d.published]
            sharevalue_before = ShareValue.objects.filter(share=d.share, time__lte=d.published,
                                                          time__gte=d.published - timedelta(minutes=time)).last()
            # first share value in the interval [d.published + time, d.published + time * 2]
            sharevalue_after = ShareValue.objects.filter(share=d.share,
                                                         time__gte=d.published + timedelta(minutes=time),
                                                         time__lte=d.published + timedelta(
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
                d.sentiment = impact
                d.save()

        relevant_docs = Document.objects.filter(published__gte=ShareValue.objects.first().time,
                                                published__lte=ShareValue.objects.last().time - timedelta(
                                                    minutes=time))

        for document in relevant_docs:

            known_feats = []
            for training_docs in relevant_docs.filter(published__lt=document.published - timedelta(minutes=time)):
                text = get_nltktext(training_docs.text)
                known_feats.append((word_feats(text), training_docs.sentiment))
                print('ja')

            if known_feats:
                classifier = NaiveBayesClassifier.train(known_feats)
                classifier.show_most_informative_features()

                # classify current document
                text = get_nltktext(document.text)
                result = classifier.classify(word_feats(text))

                document.predicted_sentiment = result
                document.save()

                calculate_credibility()

                prediction = 0
                for doc in Document.objects.filter(share=document.share,
                                                   published__gte=document.published - timedelta(minutes=time),
                                                   predicted_sentiment__isnull=False):
                    if doc.predicted_sentiment == 'pos':
                        prediction += 1 * doc.credibility
                    elif doc.predicted_sentiment == 'neg':
                        prediction += -1 * doc.credibility

                if prediction > 0:
                    result = 'pos'
                elif prediction < 0:
                    result = 'neg'
                else:
                    result = 'neu'

                ws.append([result, document.sentiment, result == document.sentiment])
                wb.save(settings.FILE)
