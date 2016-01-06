from django.core.management.base import BaseCommand
from stock_retrieval.models import Share, ShareDay
from time import gmtime, strftime
from yahoo_finance import Share as YahooShare
from datetime import datetime, timedelta


class Command(BaseCommand):
    def handle(self, *args, **options):
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
                ShareDay(share=self, volume=d['Volume'], adj_close=d['Adj_Close'], high=d['High'], low=d['Low'],
                         date=datetime.strptime(d['Date'], "%Y-%m-%d").date(), close=d['Close'], open=d['Open']).save()
