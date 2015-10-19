from django.db import models
import feedparser

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

    @staticmethod
    def synchronise():
        for stock in NewsArticle.get_feeds():
            for item in stock.entries:
                NewsArticle(stock=stock, google_id=item.id, title=item.title, link=item.link, summary=item.summary).save()

    @staticmethod
    def get_feeds():
        stock_list = []
        for stock in STOCKS:
           stock_list.append(feedparser.parse('https://news.google.com/news?q=%s&output=rss' % stock))
        return stock_list