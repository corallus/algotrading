from django.db import models
from django.utils.translation import ugettext_lazy as _

STOCKS = [('YHOO', 'Yahoo'), ('IBM', 'IBM'), ('TSLA', 'Tesla'), ('ASML.AS', 'ASML')]


class Share(models.Model):
    share = models.CharField(_('share'), max_length=31, choices=STOCKS, unique=True)

    def __str__(self):
        return self.get_share_display()


class ShareValue(models.Model):
    share = models.ForeignKey(Share, verbose_name=_('share'))
    volume = models.PositiveIntegerField(_('volume'))
    time = models.DateTimeField(_('date'))
    open = models.DecimalField(_('open'), max_digits=12, decimal_places=2)
    price = models.DecimalField(_('price'), max_digits=12, decimal_places=2)

    def __str__(self):
        return '%s - %s - %s' % (self.share, self.time, self.price)

    class Meta:
        ordering = ['time']


class ShareDay(models.Model):
    share = models.ForeignKey(Share, verbose_name=_('share'))
    volume = models.PositiveIntegerField(_('volume'))
    adj_close = models.DecimalField(_('closing value'), max_digits=12, decimal_places=2)
    high = models.DecimalField(_('highest value'), max_digits=12, decimal_places=2)
    low = models.DecimalField(_('lowest value'), max_digits=12, decimal_places=2)
    date = models.DateTimeField(_('date'))
    close = models.DecimalField(_('close'), max_digits=12, decimal_places=2)
    open = models.DecimalField(_('open'), max_digits=12, decimal_places=2)

    def __str__(self):
        return '%s - %s' % (self.share, self.date)

    class Meta:
        ordering = ['date']




