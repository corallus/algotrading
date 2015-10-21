from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from .views import SyncFeed, StockPriceList


urlpatterns = patterns(
    '',
    url(r'^$', StockPriceList.as_view(), name='stock-retrieval'),
    url(r'^sync/$', SyncFeed.as_view(), name='stock-sync'),
)