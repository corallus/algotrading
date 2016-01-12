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
