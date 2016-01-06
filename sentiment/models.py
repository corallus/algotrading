from bs4 import BeautifulSoup
from nltk.classify import NaiveBayesClassifier
import nltk

from social_retrieval.models import Tweet
from news_retrieval.models import NewsArticle


def word_feats(words):
    return dict([(word, True) for word in words])


class SentimentDocument(object):

    @staticmethod
    def train():
        pass

    @staticmethod
    def classify(classifier):
        pass


class TwitterSentiment(SentimentDocument):

    @staticmethod
    def train():
        pass

    @staticmethod
    def classify(classifier):
        pass


class NewsSentiment(SentimentDocument):

    @staticmethod
    def train():
        training_feats = []
        for article in NewsArticle.objects.training_data():
            raw = BeautifulSoup(article.description).get_text()
            tokens = nltk.word_tokenize(raw)
            text = nltk.Text(tokens)
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

    @staticmethod
    def classify(classifier):
        for article in NewsArticle.objects.new_data():
            raw = BeautifulSoup(article.description).get_text()
            tokens = nltk.word_tokenize(raw)
            text = nltk.Text(tokens)
            result = classifier.classify(word_feats(text))
            article.document.classification = result
            article.save()
