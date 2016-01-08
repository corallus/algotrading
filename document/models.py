from django.db import models

from stock_retrieval.models import Share


class Link(models.Model):
    url = models.CharField(max_length=255)

    def __str__(self):
        return self.url


class Document(models.Model):
    share = models.ForeignKey (Share)
    text = models.TextField(blank=True)
    similar = models.ForeignKey('self', null=True, default=None)  # TODO used for similar posts
    links = models.ManyToManyField(Link)  # TODO make sure all links are formatted the same
    predicted_sentiment = models.CharField('predicted sentiment', max_length=127, null=True)
    sentiment = models.CharField('sentiment', max_length=127, null=True)
    credibility = models.IntegerField(default=1)