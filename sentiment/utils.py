from bs4 import BeautifulSoup
from nltk.classify import NaiveBayesClassifier
import nltk
from datetime import timedelta, datetime
from news_retrieval.models import NewsArticle
from stock_retrieval.models import ShareValue


# from nltk.sentiment import SentimentAnalyzer http://www.nltk.org/howto/sentiment.html


def word_feats(words):
    return dict([(word, True) for word in words])


def get_sentiment(article):
    # get share value before article
    value_before = ShareValue.objects.filter(share=article.document.share, time__lt=article.published).order_by(
        'time').last().price

    # get share value x time after article
    value_after = ShareValue.objects.filter(share=article.document.share,
                                            time__gt=article.published + timedelta(hours=1)).order_by(
        'time').first().price

    if value_after > value_before:
        sentiment = 'pos'
    elif value_before > value_after:
        sentiment = 'neg'
    else:
        sentiment = 'neutral'

    article.document.sentiment = sentiment
    article.document.save()
    return sentiment


def get_text(article):
    raw = BeautifulSoup(article.description).get_text()
    tokens = nltk.word_tokenize(raw)
    return nltk.Text(tokens)


def train():
    training_feats = []
    first_share_value = ShareValue.objects.first()

    # only articles after a share value was know are interesting
    relevant_articles = NewsArticle.objects.filter(published__gt=first_share_value.time)
    relevant_articles_count = relevant_articles.count()


    for article in NewsArticle.objects.training_data():
        text = get_text(article)

        sentiment = get_sentiment(article)

        training_feats.append((word_feats(text), sentiment))

    classifier = NaiveBayesClassifier.train(training_feats)

    testing_feats = []
    for article in NewsArticle.objects.test_data():
        text = get_text(article)

        sentiment = get_sentiment(article)

        testing_feats.append((word_feats(text), sentiment))

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
        article.document.predicted_sentiment = result
        article.save()
