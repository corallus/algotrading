from dateutil import parser
from django.conf import settings
import oauth2
from document.models import Document, Link
from social_retrieval.models import Tweet
from stock_retrieval.models import Share
import json

__author__ = 'kees'

NUMBER_OF_TWEETS = 100


def fetch():
        """
        This is how the access token should be obtained, but needs a request object and logged in user
        try:
            twitter_user = self.request.user.social_auth.get(provider='twitter')
        except:
            return
        if not twitter_user.access_token:
            return
        access_token = twitter_user.access_token['oauth_token']
        access_token_secret = twitter_user.access_token['oauth_token_secret']"""

        access_token = settings.TWITTER_ACCESS_TOKEN
        access_token_secret = settings.TWITTER_ACCESS_TOKEN_SECRET

        for share in Share.objects.all():
            base_url = 'https://api.twitter.com/1.1/search/tweets.json?q=%s' % share.get_share_display()
            param_dict = {'lang': 'en', 'count': NUMBER_OF_TWEETS, 'result_type': 'recent'}

            try:
                last = Tweet.objects.filter(document__share=share).order_by('tweet_id').last()
                if last:
                    param_dict['since_id'] = last.tweet_id
            except Tweet.DoesNotExist:
                pass

            params = ''
            for key, value in param_dict.items():
                params += '&%s=%s' % (key, value)
            url = base_url + params
            print(url)  # TODO remove
            search = oauth_req(url, access_token, access_token_secret)
            str_search = search.decode('utf-8')
            tweets = json.loads(str_search)  # TODO also get the more then 100 latest tweets.
            for tweet in tweets['statuses']:
                tweet_dict = {'created_at': parser.parse(tweet['created_at']),
                              'favorite_count': tweet['favorite_count'],
                              'tweet_id': tweet['id'],  # 'retweeted_status': tweet['retweeted_status'],
                              'in_reply_to_status_id': tweet['in_reply_to_status_id'],
                              'is_quote_status': tweet['is_quote_status'], 'retweet_count': tweet['retweet_count'],
                              'text': tweet['text'], 'user_id': tweet['user']['id'],
                              'user_followers_count': tweet['user']['followers_count'],
                              'user_favourites_count': tweet['user']['favourites_count'],
                              'user_friends_count': tweet['user']['friends_count'],
                              'user_listed_count': tweet['user']['listed_count'], 'user_name': tweet['user']['name'],
                              'user_screen_name': tweet['user']['screen_name'],
                              'user_statuses_count': tweet['user']['statuses_count']
                              }
                try:
                    Tweet.objects.get(tweet_id=tweet_dict['tweet_id'])
                    break
                except Tweet.DoesNotExist:  # the tweet does not exist, so should be added
                    document = Document.objects.create(share=share, text=tweet_dict.pop('text'),
                                                       source=tweet['user']['id'], type='tw',
                                                       published=tweet['created_at'])
                    database_tweet = Tweet.objects.get_or_create(document=document, **tweet_dict)[0]
                    if 'retweeted_status' in tweet:  # this is a retweet
                        original_tweet_id = tweet['retweeted_status']['id']
                        try:
                            # set this as a retweet
                            original_tweet = Tweet.objects.get(tweet_id=original_tweet_id)
                            database_tweet.original = original_tweet
                            database_tweet.save()
                            original_document = Document.objects.get(tweet=original_tweet)
                            document.similar = original_document
                            document.save()
                            print('tweet id ' + str(database_tweet.tweet_id) + ' original set')
                        except Tweet.DoesNotExist:
                            print('tweet ' + str(original_tweet_id) + ' does not exist')  # TODO create this tweet
                    if tweet['entities']['urls']:  # these are the urls
                        urls = []
                        for url in tweet['entities']['urls']:
                            link = Link.objects.get_or_create(url=url['expanded_url'])[0]
                            link.save()
                            urls.append(link)
                        document.links.add(*urls)


def oauth_req(url, key, secret, http_method="GET", body="".encode(), http_headers=None):
    consumer = oauth2.Consumer(key=settings.SOCIAL_AUTH_TWITTER_KEY, secret=settings.SOCIAL_AUTH_TWITTER_SECRET)
    token = oauth2.Token(key=key, secret=secret)
    client = oauth2.Client(consumer, token)
    resp, content = client.request(url, method=http_method, body=body, headers=http_headers)
    return content
