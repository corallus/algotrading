from django.db import models
from datetime import datetime, timedelta

from stock_retrieval.models import Share
from document.models import Document


class DocumentManager(models.Manager):

    def training_data(self):
        return super(DocumentManager, self).get_queryset().filter(published__lte=datetime.now()-timedelta(days=2))

    def test_data(self):
        return super(DocumentManager, self).get_queryset().filter(published__lte=datetime.now()-timedelta(days=1),
                                                                  published__gte=datetime.now()-timedelta(days=2))

    def new_data(self):
        return super(DocumentManager, self).get_queryset().filter(published__gte=datetime.now()-timedelta(days=1))


class NewsArticle(models.Model):
    document = models.OneToOneField(Document)
    guid = models.CharField('guid', max_length=200)
    link = models.CharField('link', max_length=400)
    source = models.CharField('source', max_length=400)
    published = models.DateTimeField('published')
    description = models.TextField('description')
    title = models.CharField('title', max_length=200)
    enclosure = models.CharField('enclosure', max_length=400)
    category = models.CharField('category', max_length=127)
    objects = DocumentManager()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['published']
