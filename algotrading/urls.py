"""
algotrading URL Configuration
"""
from django.conf.urls import include, url
from django.contrib import admin
import credibility.urls
import news_retrieval.urls
import social_retrieval.urls
from django.views.generic import TemplateView
import indexer.urls
import stock_retrieval.urls
import summarize.urls
import sentiment.urls

urlpatterns = [
    url(r'^authenticate/', include('social.apps.django_app.urls', namespace='social')),
    url(r'^indexer/', include(indexer.urls)),
    url(r'^credibility/', include(credibility.urls)),
    url(r'^news-retrieval/', include(news_retrieval.urls)),
    url(r'^social-retrieval/', include(social_retrieval.urls)),
    url(r'^stock-retrieval/', include(stock_retrieval.urls)),
    url(r'^summarizer/', include(summarize.urls)),
    url(r'^sentiment/', include(sentiment.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', TemplateView.as_view(template_name="dashboard.html"), name='dashboard'),
]
