from stock_retrieval.models import Share, ShareDay, ShareValue
from time import gmtime, strftime
from yahoo_finance import Share as YahooShare
from datetime import datetime, timedelta
from django.conf import settings


def fetch():
    for share in Share.objects.all():
        try:
            sh = YahooShare(share.share)
        except:
            print('exception occurred while fetching stock...')
            continue

        sv, created = ShareValue.objects.get_or_create(share=share, price=sh.get_price(), open=sh.get_open(),
                                                       volume=sh.get_volume(),
                                                       time=datetime.strptime(sh.get_trade_datetime(),
                                                                              '%Y-%m-%d %H:%M:%S %Z%z'))
        if not created:
            print('%s market is closed' % sv.share)
        else:
            for database in settings.DATABASES:
                sv.save(using=database)


def fetch_historical():
    for share in Share.objects.all():
        yahoo = YahooShare(share.share)
        last_retrieved = share.shareday_set.filter(share=share.pk).order_by('date').last()
        if last_retrieved:
            retrieve_from = last_retrieved.date + timedelta(days=1)
            retrieve_from = retrieve_from.strftime("%Y-%m-%d")
        else:
            retrieve_from = '2015-01-01'

        data = yahoo.get_historical(retrieve_from, strftime("%Y-%m-%d", gmtime()))

        for d in data:
            ShareDay(share=share, volume=d['Volume'], adj_close=d['Adj_Close'], high=d['High'], low=d['Low'],
                     date=datetime.strptime(d['Date'], "%Y-%m-%d").date(), close=d['Close'], open=d['Open']).save()
