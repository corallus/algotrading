from bs4 import BeautifulSoup
from nltk.classify import NaiveBayesClassifier
import nltk

from news_retrieval.models import NewsArticle
from stock_retrieval.models import ShareDay


def word_feats(words):
    return dict([(word, True) for word in words])


def train():
    training_feats = []
    for article in NewsArticle.objects.training_data():
        raw = BeautifulSoup(article.description).get_text()
        tokens = nltk.word_tokenize(raw)
        text = nltk.Text(tokens)

        # get share value before article
        shareday = ShareDay.objects.filter(share=article.document.share, date__lt=article.published).order_by('date').first()
        shareday.close

        # get share value after article
        shareday = ShareDay.objects.filter(share=article.document.share, date__lt=article.published).order_by('date').first()
        shareday.open

        training_feats.append((word_feats(text), 'pos'))

    classifier = NaiveBayesClassifier.train(training_feats)

    testing_feats = []
    for article in NewsArticle.objects.test_data():
        raw = BeautifulSoup(article.description).get_text()
        tokens = nltk.word_tokenize(raw)
        text = nltk.Text(tokens)
        testing_feats.append((word_feats(text), 'pos'))

    print('train on %d instances, test on %d instances' % (len(training_feats), len(testing_feats)))

    print('accuracy:', nltk.classify.util.accuracy(classifier, testing_feats))
    classifier.show_most_informative_features()

    return classifier


def classify(classifier):
    for article in NewsArticle.objects.new_data():
        raw = BeautifulSoup(article.description).get_text()
        tokens = nltk.word_tokenize(raw)
        text = nltk.Text(tokens)
        result = classifier.classify(word_feats(text))
        article.document.classification = result
        article.save()
