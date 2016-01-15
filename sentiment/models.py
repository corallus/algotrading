from django.db import models
from stock_retrieval.models import Share


class Prediction(models.Model):
    share = models.ForeignKey(Share)
    prediction = models.IntegerField('prediction')
