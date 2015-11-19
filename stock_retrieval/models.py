from django.db import models
from django.utils.translation import ugettext_lazy as _
from time import gmtime, strftime
from yahoo_finance import Share as YahooShare
from datetime import datetime, timedelta

STOCKS = [('YHOO', 'Yahoo'), ('IBM', 'IBM'), ('TSLA', 'Tesla'), ('ASML.AS', 'ASML')]


class Share(models.Model):
    share = models.CharField(_('share'), max_length=31, choices=STOCKS)

    def get_historical(self):
        yahoo = YahooShare(self.share)
        last_retrieved = self.shareday_set.last()
        if last_retrieved:
            retrieve_from = last_retrieved.date() + timedelta(days=1)
            retrieve_from = strftime("%Y-%m-%d", retrieve_from)
        else:
            retrieve_from = '2015-01-01'

        data = yahoo.get_historical(retrieve_from, strftime("%Y-%m-%d", gmtime()))
        print(data)

        for d in data:
            ShareDay(share=self, volume=d['Volume'], adj_close=d['Adj_Close'], high=d['High'], low=d['Low'],
                     date=datetime.strptime(d['Date'], "%Y-%m-%d").date(), close=d['Close'], open=d['Open']).save()

    def __str__(self):
        return self.get_share_display()


class ShareDay(models.Model):
    share = models.ForeignKey(Share, verbose_name=_('share'))
    volume = models.PositiveIntegerField(_('volume'))
    adj_close = models.DecimalField(_('closing value'), max_digits=12, decimal_places=2)
    high = models.DecimalField(_('highest value'), max_digits=12, decimal_places=2)
    low = models.DecimalField(_('lowest value'), max_digits=12, decimal_places=2)
    date = models.DateField(_('date'))
    close = models.DecimalField(_('close'), max_digits=12, decimal_places=2)
    open = models.DecimalField(_('open'), max_digits=12, decimal_places=2)

    def __str__(self):
        return '%s - %s' % (self.share, self.date)

    class Meta:
        ordering = ['-date']

