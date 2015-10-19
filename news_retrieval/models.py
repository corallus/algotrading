from django.db import models


class NewsArticle(models.Model):
    google_id = models.CharField('id', max_length=200)
    link = models.CharField('link', max_length=400)
    published = models.DateTimeField('published')
    summary = models.TextField('summary')
    title = models.CharField('title', max_length=200)

    def __str__(self):
        return self.title