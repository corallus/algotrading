"""algotrading URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
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
