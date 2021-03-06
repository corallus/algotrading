from dateutil import parser
from django.conf import settings
from django.db import transaction
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
        base_url = 'https://api.twitter.com/1.1/search/tweets.json?q=%23'
        base_url += share.get_share_display()
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
        search = oauth_req(url, access_token, access_token_secret)
        str_search = search.decode('utf-8')
        tweets = json.loads(str_search)  # TODO also get the more then 100 latest tweets.
        if not 'statuses' in tweets:
            return False  # No new statuses
        with transaction.atomic():
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
                              'user_listed_count': tweet['user']['listed_count'],
                              'user_screen_name': tweet['user']['screen_name'],
                              'user_statuses_count': tweet['user']['statuses_count']
                              }
                try:
                    Tweet.objects.get(tweet_id=tweet['id'])
                    continue  # this tweet is already in the database
                except Tweet.DoesNotExist:
                    pass

                document = Document.objects.create(share=share, text=tweet_dict.pop('text'),
                                                   source=tweet['user']['id'], type='tw',
                                                   published=tweet_dict['created_at'])
                database_tweet = Tweet.objects.create(document=document, **tweet_dict)
                '''
                if tweet['entities']['urls']:  # these are the urls
                    urls = []
                    for url in tweet['entities']['urls']:
                        link = Link.objects.get_or_create(url=url['expanded_url'])[0]
                        urls.append(link)
                    document.links.add(*urls)'''
        with transaction.atomic():
            for tweet in tweets['statuses']:
                if 'retweeted_status' in tweet:  # this is a retweet
                    original_tweet_id = tweet['retweeted_status']['id']
                    try:
                        # set this as a retweet
                        retweet = Tweet.objects.get(tweet_id=tweet['id'])
                        original_tweet = Tweet.objects.get(tweet_id=original_tweet_id)
                        retweet.original = original_tweet
                        retweet.save()
                        document = Document.objects.get(tweet=retweet)
                        original_document = Document.objects.get(tweet=original_tweet)
                        document_in_database = Document.objects.get(id=document.id)
                        original_in_database = Document.objects.get(id=original_document.id)
                        document_in_database.similar = original_in_database
                        document_in_database.save()
                        # print('tweet id ' + str(database_tweet.tweet_id) + ' original set')
                    except Tweet.DoesNotExist:
                        pass
                        # print('tweet ' + str(original_tweet_id) + ' does not exist')  # TODO create this tweet
    return True


def oauth_req(url, key, secret, http_method="GET", body="".encode(), http_headers=None):
    consumer = oauth2.Consumer(key=settings.SOCIAL_AUTH_TWITTER_KEY, secret=settings.SOCIAL_AUTH_TWITTER_SECRET)
    token = oauth2.Token(key=key, secret=secret)
    client = oauth2.Client(consumer, token)
    resp, content = client.request(url, method=http_method, body=body, headers=http_headers)
    return content
