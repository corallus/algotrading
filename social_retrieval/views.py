import hashlib
import random
from time import time
from urllib import request as url_request
import urllib.parse
from django.conf import settings
from django.core.serializers import json
from django.utils.baseconv import base64
from django.views.generic import TemplateView
import oauth2

STOCKS = ['toyota', 'netflix', 'asml', 'volkswagen']


class FacebookView(TemplateView):
    template_name = 'news_retrieval/index.html'

    def get_context_data(self, **kwargs):
        context = super(FacebookView, self).get_context_data(**kwargs)
        context.update({
            'stock_list': self.get_feeds()
        })
        return context

    def get_feeds(self):
        social_user = self.request.user.social_auth.filter(
            provider='twitter',).first()
        if social_user:
            url = u'https://graph.facebook.com/{0}/' \
            u'friends?fields=id,name,location,picture' \
            u'&access_token={1}'.format(
            social_user.uid,
            social_user.extra_data['access_token'],
            )

        stock_list = []
        for stock in STOCKS:
            pass
            # stock_list.append(feedparser.parse('https://news.google.com/news?q=%s&output=rss' % stock))
        return stock_list


class TwitterView(TemplateView):
    template_name = 'news_retrieval/index.html'

    def get_context_data(self, **kwargs):
        context = super(TwitterView, self).get_context_data(**kwargs)
        context.update({
            'stock_list': self.get_feeds()
        })
        return context

    def oauth_req(self, url, key, secret, http_method="GET", body="", http_headers=None):
        consumer = oauth2.Consumer(key=settings.SOCIAL_AUTH_TWITTER_KEY, secret=settings.SOCIAL_AUTH_TWITTER_SECRET)
        token = oauth2.Token(key=key, secret=secret)
        client = oauth2.Client(consumer, token)
        resp, content = client.request(url, method=http_method, body=body, headers=http_headers)
        return content

    def get_feeds(self):
        stock_list = []

        try:
            twitter_user = self.request.user.social_auth.get(provider='twitter')
        except:
            return
        if not twitter_user.access_token:
            return
        access_token = twitter_user.access_token['oauth_token']
        access_token_secret = twitter_user.access_token['oauth_token_secret']

        for stock in STOCKS:
            search = self.oauth_req('https://api.twitter.com/1.1/search/tweets.json?q=%s' % stock,
                                    access_token, access_token_secret)
            print(search)
        return stock_list
