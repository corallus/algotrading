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

    exists = False
    for article in articles:
        if article.outgoing.exists():
            exists = True
    if not exists:
        return  # there are no links Hits can not run

    for article in articles:
        article.hub = 1
    for step in range(ITERATIONS):
        # update the auth scores
        norm = 0
        for article in articles:
            article.auth = 0
            for incoming in article.incoming.all():
                article.auth += incoming.hub
            norm += article.auth * article.auth
        norm = sqrt(norm)
        for article in articles:
            article.auth /= norm
        # update the hub scores
        norm = 0
        for article in articles:
            article.hub = 0
            for outgoing in article.outgoing.all():
                article.hub += outgoing.auth
            norm += article.hub * article.hub
        norm = sqrt(norm)
        for article in articles:
            article.hub /= norm

    max_auth = 0
    max_hub = 0
    with transaction.atomic():
        for article in articles:
            article.save()  # save the new values in the database
            max_auth = max(max_auth, article.auth)
            max_hub = max(max_hub, article.hub)

    print('max auth ' + str(max_auth))  # TODO remove
    print('max hub ' + str(max_hub))  # TODO remove
