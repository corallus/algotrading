import codecs
import json
from django.conf import settings
from django.views.generic import TemplateView
import oauth2
from social_retrieval.models import Tweet
from time import strptime, strftime

STOCKS = ['toyota', 'netflix', 'asml', 'volkswagen']
SINCE_ID = {stock: -1 for stock in STOCKS}


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
            baseurl = 'https://api.twitter.com/1.1/search/tweets.json?q=%s' % stock
            paramdict = {'lang': 'en', 'count': 100}
            if SINCE_ID[stock] != -1:
                paramdict['since_id'] = SINCE_ID[stock]
            params = ''
            for key, value in paramdict.items():
                params += '&%s=%s' % (key, value)
            url = baseurl + params
            print(url)
            search = self.oauth_req(url, access_token, access_token_secret)
            str_search = search.decode('utf-8')
            dict = json.loads(str_search)
            for tweet in dict['statuses']:
                tweet_dict = {'created_at': strftime('%Y-%m-%d %H:%M:%S', strptime(tweet['created_at'], '%a %b %d %H:%M:%S +0000 %Y')),
                              'favorite_count': tweet['favorite_count'],
                              'tweet_id': tweet['id'], 'in_reply_to_status_id': tweet['in_reply_to_status_id'],
                              'is_quote_status': tweet['is_quote_status'], 'retweet_count': tweet['retweet_count'],
                              'text': tweet['text'], 'user_id': tweet['user']['id'],
                              'user_followers_count': tweet['user']['followers_count'],
                              'user_favourites_count': tweet['user']['favourites_count'],
                              'user_friends_count': tweet['user']['friends_count'],
                              'user_listed_count': tweet['user']['listed_count'], 'user_name': tweet['user']['name'],
                              'user_screen_name': tweet['user']['screen_name'],
                              'user_statuses_count': tweet['user']['statuses_count']
                              }
                Tweet.objects.create(**tweet_dict)
                stock_list.append(tweet_dict)
                SINCE_ID[stock] = max(SINCE_ID[stock], tweet['id'])

        return stock_list
