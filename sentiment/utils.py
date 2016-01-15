from nltk.classify import NaiveBayesClassifier
import nltk
from datetime import timedelta
from document.models import Document
from stock_retrieval.models import ShareValue

from nltk.classify import NaiveBayesClassifier
from nltk.corpus import subjectivity
from nltk.sentiment import SentimentAnalyzer
from nltk.sentiment.util import *


# from nltk.sentiment import SentimentAnalyzer http://www.nltk.org/howto/sentiment.html


def word_feats(words):
    return dict([(word, True) for word in words])


def get_impact(document, minutes_after_article):
    # get share value before article
    sharevalue_before = ShareValue.objects.filter(share=document.share, time__lt=document.published).last()

    if sharevalue_before:
        price_before = sharevalue_before.price
    else:
        document.active = False
        return None

    # get share value x time after article
    sharevalue_after = ShareValue.objects.filter(share=document.share, time__gt=document.published + timedelta(
        minutes=minutes_after_article)).first()

    if sharevalue_after:
        price_after = sharevalue_after.price
    else:
        return None

    if price_after > price_before:
        impact = 'pos'
    elif price_before > price_after:
        impact = 'neg'
    else:
        impact = 'neu'

    document.sentiment = impact
    document.save()


def get_nltktext(text):
    tokens = nltk.word_tokenize(text)
    return nltk.Text(tokens)


def train(minutes_after_article):
    # get impact for documents for which it has not been computed yet
    for document in Document.objects.filter(sentiment__isnull=True):
        get_impact(document, minutes_after_article)

    known_data = Document.objects.filter(sentiment__isnull=False)
    known_data_count = known_data.count()
    if known_data_count == 0:
        return None

    # 2/3 training data
    num_training_data = int(round(2 * known_data_count / 3))
    training_feats = []
    for document in known_data.order_by('id')[:num_training_data]:
        text = get_nltktext(document.text)
        training_feats.append((word_feats(text), document.sentiment))

    classifier = NaiveBayesClassifier.train(training_feats)

    # 1/3 test_data
    num_testing_data = int(round(known_data_count / 3))
    testing_feats = []
    for document in known_data.order_by('-id')[:num_testing_data]:
        text = get_nltktext(document.text)
        testing_feats.append((word_feats(text), document.sentiment))

    print('train on %d instances, test on %d instances' % (len(training_feats), len(testing_feats)))
    accuracy = nltk.classify.util.accuracy(classifier, testing_feats)
    print('accuracy:', accuracy)

    return classifier, accuracy


def classify(classifier):
    for document in Document.objects.filter(predicted_sentiment__isnull=True):
        text = get_nltktext(document.text)
        result = classifier.classify(word_feats(text))
        document.predicted_sentiment = result
        document.save()
