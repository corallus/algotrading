from django.db import models

from stock_retrieval.models import Share


class Link(models.Model):
    url = models.CharField(max_length=255)

    def __str__(self):
        return self.url


class Document(models.Model):
    share = models.ForeignKey(Share)
    source = models.TextField(max_length=400)
    published = models.DateTimeField('published')
    title = models.CharField('title', max_length=200)
    text = models.TextField(blank=True)
    similar = models.ForeignKey('self', null=True, default=None)  # TODO news part
    links = models.ManyToManyField(Link)  # TODO make sure all links are formatted the same
    predicted_sentiment = models.CharField('predicted sentiment', max_length=127, null=True)
    sentiment = models.CharField('sentiment', max_length=127, null=True)
    credibility = models.IntegerField(default=1)
    guid = models.CharField('guid', max_length=200)
    type = models.CharField(max_length=10, choices=[('na', 'news article'), ('tw', 'tweet')])

    def __str__(self):
        if self.title:
            return self.title
        else:
            return self.text

    class Meta:
        ordering = ['published']
