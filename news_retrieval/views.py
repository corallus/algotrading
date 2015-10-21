from django.views.generic import TemplateView, FormView, ListView
import math
import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import movie_reviews
import pprint

from .forms import SyncFeedForm
from .models import NewsArticle
from django.core.urlresolvers import reverse_lazy

"""
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
"""

class NewsArticleList(ListView):
    template_name = 'news_retrieval/index.html'
    model = NewsArticle

    def get_context_data(self, **kwargs):
        context = super(NewsArticleList, self).get_context_data(**kwargs)
        context.update({
            'training_data': NewsArticle.objects.training_data(),
            'test_data': NewsArticle.objects.test_data(),
            'new_data': NewsArticle.objects.new_data()
        })
        return context


class SyncFeed(FormView):
    form_class = SyncFeedForm
    success_url = reverse_lazy('news-retrieval')

    def form_valid(self, form):
        NewsArticle.synchronise()
        return super(SyncFeed, self).form_valid(form)


