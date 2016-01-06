from django.db import models, transaction
from math import sqrt

from document.models import Document

ITERATIONS = 5


class CredibilityModel(models.Model):
    outgoing = models.ManyToManyField('self', related_name='incoming', symmetrical=False)
    document = models.OneToOneField(Document, null=True)
    hub = models.FloatField(default=1)
    auth = models.FloatField(default=1)

    def __str__(self):
        return str(self.document)


def calculate_HITS():
    """
    Implements the HITS algorithm
    https://en.wikipedia.org/wiki/HITS_algorithm

    :return:
    """


    articles = list(CredibilityModel.objects.all())

    def get_tweet(tweet):
        for article in articles:
            if article.tweet == tweet:
                return article
        raise CredibilityModel.DoesNotExist()

    for article in articles:
        article.hub = 1
    for step in range(ITERATIONS):
        print(step)
        # update the auth scores
        norm = 0
        for article in articles:
            article.auth = 0
            for base_model_incoming in article.incoming.all():
                incoming = get_tweet(base_model_incoming.tweet)
                article.auth += incoming.hub
            norm += article.auth * article.auth
        norm = sqrt(norm)
        for article in articles:
            article.auth /= norm
        #update the hub scores
        norm = 0
        for article in articles:
            article.hub = 0
            for base_model_outgoing in article.outgoing.all():
                outgoing = get_tweet(base_model_outgoing.tweet)
                article.hub += outgoing.auth
            norm += article.hub * article.hub
        norm = sqrt(norm)
        for article in articles:
            article.hub /= norm

    max_auth = 0  # TODO remove
    max_hub = 0  # TODO remove
    with transaction.atomic():
        for article in articles:
            article.save()  # save the new values in the database
            max_auth = max(max_auth, article.auth)
            max_hub = max(max_hub, article.hub)

    print('max auth ' + str(max_auth))
    print('max hub ' + str(max_hub))
