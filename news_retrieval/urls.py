from django.conf.urls import patterns, url
from .views import NewsArticleList


urlpatterns = patterns(
    '',
    url(r'^$', NewsArticleList.as_view(), name='news-retrieval'),
)