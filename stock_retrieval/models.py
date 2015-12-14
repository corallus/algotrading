from django.db import models
from django.utils.translation import ugettext_lazy as _
import urllib.request as ur
import re
from datetime import  datetime


STOCKS = [('toyoya', 'toyota'), ('netflix', 'netflix'), ('asml', 'asml'), ('volkswagen', 'volkswagen')]


class Stock(models.Model):
    display_name = models.CharField(verbose_name=(_('stock')), max_length=127)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.display_name

    @staticmethod
    def get_stocks():
        for stock in Stock.objects.all():
            url = "http://finance.yahoo.com/q?s=" + stock.slug + "&ql=1"
            html_file = ur.urlopen(url)
            html_text = html_file.read()
            regex = '<span id="yfs_l84_' + stock.slug + '">(.+?)</span>'
            regex = regex.encode('utf-8')
            pattern = re.compile(regex)
            price = re.findall(pattern, html_text)
            print(price)
            stock_price = StockPrice(price=price[0], stock=stock)
            stock_price.save()


class StockPrice(models.Model):
    published = models.DateTimeField('published', auto_now_add=True)
    stock = models.ForeignKey(Stock, verbose_name='stock')
    price = models.FloatField('price')

    def __str__(self):
        return str(self.price)

    class Meta:
        ordering = ['stock', 'published']


