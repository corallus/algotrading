from django.views.generic import TemplateView
from credibility.models import HITS, calculate_HITS
from social_retrieval.models import Tweet

__author__ = 'vincent'


def convert_tweet_to_graph():
    tweets = Tweet.objects.all()
    for tweet in tweets:
        HITS.objects.get_or_create(tweet=tweet)
    for tweet in tweets:
        if tweet.original:
            hit = HITS.objects.get(tweet=tweet)
            original = HITS.objects.get(tweet=tweet.original)
            hit.outgoing.add(original)


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

        # source (Non twitter)

        # previously correct
        pass

    def update_hub_authority(self, person):
        # make a graph connection from every hub to authority, create when necessary  # TODO also add to crawler
        pass

    def update_hub(self, person):
        pass

    def update_authority(self, person):
        pass

