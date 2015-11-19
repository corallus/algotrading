from django.conf.urls import patterns, url
from .views import SyncFeed, ShareDayList


urlpatterns = patterns(
    '',
    url(r'^$', ShareDayList.as_view(), name='stock-retrieval'),
    url(r'^sync/$', SyncFeed.as_view(), name='stock-sync'),
)