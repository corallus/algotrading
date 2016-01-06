from django.conf.urls import patterns, url
from .views import SyncFeed, ShareDayList, CreateShareView


urlpatterns = patterns(
    '',
    url(r'^$', ShareDayList.as_view(), name='stock-retrieval'),
    url(r'^create/$', CreateShareView.as_view(), name='stock-create'),
    url(r'^sync/$', SyncFeed.as_view(), name='stock-sync'),
)