from django.views.generic import TemplateView
import feedparser
import math
import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import movie_reviews
from bs4 import BeautifulSoup
import pprint

STOCKS = ['toyota', 'netflix', 'asml', 'volkswagen']


def word_feats(words):
    return dict([(word, True) for word in words])

negids = movie_reviews.fileids('neg')
posids = movie_reviews.fileids('pos')

negfeats = [(word_feats(movie_reviews.words(fileids=[f])), 'neg') for f in negids]
posfeats = [(word_feats(movie_reviews.words(fileids=[f])), 'pos') for f in posids]

negcutoff = int(math.floor(len(negfeats)*3/4))
poscutoff = int(math.floor(len(posfeats)*3/4))

trainfeats = negfeats[:negcutoff] + posfeats[:poscutoff]
testfeats = negfeats[negcutoff:] + posfeats[poscutoff:]
print('train on %d instances, test on %d instances' % (len(trainfeats), len(testfeats)))

classifier = NaiveBayesClassifier.train(trainfeats)
print('accuracy:', nltk.classify.util.accuracy(classifier, testfeats))
classifier.show_most_informative_features()


class NewsFeeds(TemplateView):
    template_name = 'news_retrieval/index.html'

    def get_context_data(self, **kwargs):
        context = super(NewsFeeds, self).get_context_data(**kwargs)
        stocks = self.get_feeds()
        for stock in stocks:
            for feed in stock.entries:
                pass
                #raw = BeautifulSoup(feed.description).get_text()
                #feed.status = classifier.classify(raw)

        pp = pprint.PrettyPrinter(indent=4)

        context.update({
            'stock_list': stocks,
            'pp': '1'
        })
        pp.pprint(stocks[0].entries[0])
        return context

    def get_feeds(self):
        stock_list = []
        for stock in STOCKS:
           stock_list.append(feedparser.parse('https://news.google.com/news?q=%s&output=rss' % stock))
        return stock_list
