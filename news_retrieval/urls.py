from django.conf.urls import patterns, url
from .views import NewsFeeds, SyncFeed


urlpatterns = patterns(
    '',
    url(r'^$', NewsFeeds.as_view(), name='news-retrieval'),
    url(r'^$', SyncFeed.as_view(), name='news-sync'),
)