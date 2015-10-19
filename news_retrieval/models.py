from django.db import models
import feedparser
from datetime import datetime

STOCKS = [('toyoya', 'toyota'), ('netflix', 'netflix'), ('asml', 'asml'), ('volkswagen', 'volkswagen')]


class NewsArticle(models.Model):
    google_id = models.CharField('id', max_length=200)
    link = models.CharField('link', max_length=400)
    published = models.DateTimeField('published')
    summary = models.TextField('summary')
    title = models.CharField('title', max_length=200)
    stock = models.CharField(choices=STOCKS, max_length=127)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['published']

    @staticmethod
    def synchronise():
        for stock in STOCKS:
            feed = NewsArticle.get_feed(stock[0])
            for item in feed.entries:
                if not NewsArticle.objects.filter(google_id=item.id).exists():
                    NewsArticle(stock=stock[0], google_id=item.id, title=item.title, link=item.link,
                                summary=item.summary,
                                published=datetime.strptime(item.published, '%a, %d %b %Y %H:%M:%S %Z')).save()

    @staticmethod
    def get_feed(stock):
        articles = feedparser.parse('https://news.google.com/news?q=%s&output=rss' % stock)
        return articles
