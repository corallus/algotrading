from django.db import models
import feedparser
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
from nltk.classify import NaiveBayesClassifier
import nltk
from stock_retrieval.models import STOCKS


class DocumentManager(models.Manager):

    def training_data(self):
        return super(DocumentManager, self).get_queryset().filter(published__lte=datetime.now()-timedelta(days=2))

    def test_data(self):
        return super(DocumentManager, self).get_queryset().filter(published__lte=datetime.now()-timedelta(days=1),
                                                                  published__gte=datetime.now()-timedelta(days=2))

    def new_data(self):
        return super(DocumentManager, self).get_queryset().filter(published__gte=datetime.now()-timedelta(days=1))


def word_feats(words):
    return dict([(word, True) for word in words])


class NewsArticle(models.Model):
    guid = models.CharField('guid', max_length=200)
    link = models.CharField('link', max_length=400)
    source = models.CharField('source', max_length=400)
    published = models.DateTimeField('published')
    description = models.TextField('description')
    title = models.CharField('title', max_length=200)
    stock = models.CharField(choices=STOCKS, max_length=127)
    enclosure = models.CharField('enclosure', max_length=400)
    category = models.CharField('category', max_length=127)
    classification = models.CharField('classification', max_length=127)
    objects = DocumentManager()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['published']

    @staticmethod
    def synchronise():
        for stock in STOCKS:
            feed = NewsArticle.get_feed(stock[0])
            for item in feed.entries:
                if not NewsArticle.objects.filter(guid=item.guid).exists():
                    NewsArticle(stock=stock[0], guid=item.guid, title=item.title, link=item.link,
                                description=item.description,
                                published=datetime.strptime(item.published, '%a, %d %b %Y %H:%M:%S %Z')).save()
        classifier = NewsArticle.train()
        NewsArticle.classify(classifier)

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
            print(result)
            article.classification = result
            article.save()

    @staticmethod
    def get_feed(stock):
        articles = feedparser.parse('https://news.google.com/news?q=%s&output=rss' % stock)
        return articles
