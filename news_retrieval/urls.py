from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from .views import NewsFeeds


urlpatterns = patterns(
    '',
    url(r'^$', NewsFeeds.as_view(), name='news-retrieval'),
)