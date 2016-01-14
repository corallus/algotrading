from django.db import models, transaction
from math import sqrt
from django.db.models import Sum, Max

from document.models import Document

ITERATIONS = 5
SOURCE_WEIGHT = 1
HITS_WEIGHT = 1  # the auth score is taken, so gets higher when more retweete


class SourceModel(models.Model):
    document_source = models.TextField(max_length=400)
    source_correct = models.FloatField(default=0)
    total = models.FloatField(default=0)


class CredibilityModel(models.Model):
    outgoing = models.ManyToManyField('self', related_name='incoming', symmetrical=False)
    document = models.OneToOneField(Document, null=True)
    hub = models.FloatField(default=0)
    auth = models.FloatField(default=0)
    source_score = models.FloatField(default=0)
    credibility = models.FloatField(default=1)
    source = models.ForeignKey(SourceModel, related_name='credibility_models', null=True)

    def __str__(self):
        return str(self.document)


def convert_document_to_graph():
    print('constructing graph...')  # TODO log
    documents = Document.objects.all()
    with transaction.atomic():
        for document in documents:
            model = CredibilityModel.objects.get_or_create(document=document)[0]
            if document.source:
                source = SourceModel.objects.get_or_create(document_source=document.source)[0]
                model.source = source
                model.save()
    for document in documents:
        if document.similar:
            # this document is similar to another document, so create a link to the original (first)
            similar_model = CredibilityModel.objects.get(document=document)  # TODO loop over credibility model instead
            original = CredibilityModel.objects.get(document=document.similar)
            similar_model.outgoing.add(original)


def set_credibility():
    print('setting credibility...')  # TODO log
    with transaction.atomic():
        for credibility_model in CredibilityModel.objects.all():
            credibility = 1
            credibility += credibility_model.source_score * SOURCE_WEIGHT
            credibility += credibility_model.auth * HITS_WEIGHT
            credibility_model.credibility = credibility
            credibility_model.save()
            credibility_model.document.credibility = credibility
            credibility_model.document.save()


def calculate_hits():
    """
    Implements the HITS algorithm
    https://en.wikipedia.org/wiki/HITS_algorithm

    :return:
    """
    print('calculating hits...')  # TODO log

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

    with transaction.atomic():
        for article in articles:
            article.save()  # save the new values in the database

    maxima = CredibilityModel.objects.aggregate(Max('auth'), Max('hub'), Max('incoming'))
    print('max auth ' + str(maxima['auth__max']))  # TODO log
    print('max hub ' + str(maxima['hub__max']))  # TODO log
    print('max incoming ' + str(maxima['incoming__max']))  # TODO log


def calculate_source_correctness():
    print('calculating source...')  # TODO log
    with transaction.atomic():
        for source in SourceModel.objects.all():
            # first make sure to set everything back to zero.
            source.source_correct = 0
            source.total = 0

            # check all documents connected to this source
            for credibility_model in source.credibility_models.all():
                # check if we already know if correct
                if not credibility_model.document.sentiment:
                    continue
                    # we do not know the impact yet, so skip this document
                if not credibility_model.document.predicted_sentiment:
                    continue
                    # this article was not predicted is used for training instead
                source.total += 1
                # we know the impact of this document so total + 1
                if credibility_model.document.sentiment == credibility_model.document.predicted_sentiment:
                    source.source_correct += 1
            source.save()

    total_sum = SourceModel.objects.aggregate(Sum('total'))['total__sum']

    with transaction.atomic():
        for credibility_model in CredibilityModel.objects.all():
            if not credibility_model.source:
                continue
                # not source, so we dont have to do anything :)
            source = credibility_model.source
            if source.total == 0:
                continue
                # source has not got a result yet (prediction is not checked yet)
            score = source.source_correct * source.source_correct
            score /= (source.total * total_sum)
            credibility_model.source_score = score
            credibility_model.save()

    print('max source: '+str(CredibilityModel.objects.aggregate(Max('source_score'))['source_score__max']))  # TODO log


def calculate_credibility():
    convert_document_to_graph()
    calculate_hits()
    calculate_source_correctness()
    set_credibility()
