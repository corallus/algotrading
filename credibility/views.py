from django.views.generic import TemplateView
from credibility.models import CredibilityModel, calculate_HITS
from social_retrieval.models import Tweet

__author__ = 'vincent'


def convert_tweet_to_graph():
    tweets = Tweet.objects.all()
    for tweet in tweets:
        CredibilityModel.objects.get_or_create(document=tweet.document)
    for tweet in tweets:
        if tweet.original:
            retweet = CredibilityModel.objects.get(
                document=tweet.document)  # This is a retweet, so link to the original
            original = CredibilityModel.objects.get(document=tweet.original.document)
            retweet.outgoing.add(original)


def calculate_hits():
    convert_tweet_to_graph()
    # TODO convert_news_to_graph()

    calculate_HITS()
    return


class HITSView(TemplateView):
    template_name = 'credibility/hits.html'

    def get_context_data(self, **kwargs):
        context = super(HITSView, self).get_context_data(**kwargs)
        context.update({
            'hits': calculate_hits()
        })
        return context


class CredibilityView(TemplateView):
    template_name = 'credibility/index.html'

    def get_context_data(self, **kwargs):
        context = super(CredibilityView, self).get_context_data(**kwargs)
        context.update({
            'credibility': self.get_credibility()
        })
        return context

    def get_credibility(self, *people):

        result = []
        for person in people:
            credibility = (person, person.get_credibility())
            result.append(credibility)
        return result

    def set_credibility(self, *people):
        # people is a list with all given people

        # hub, authority

        # page Rank

        # source (Newspaper or twitter author)

        # previously correct
        pass