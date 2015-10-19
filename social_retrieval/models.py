from django.db import models

# Create your models here.


class Tweet(models.Model):

    tweet_id = models.IntegerField()
    created_at = models.DateTimeField()
    favorite_count = models.IntegerField()
    in_reply_to_status_id = models.IntegerField(null=True)
    is_quote_status = models.BooleanField()
    retweet_count = models.IntegerField()
    text = models.TextField()
    user_id = models.IntegerField()
    user_followers_count = models.IntegerField()
    user_favourites_count = models.IntegerField()
    user_friends_count = models.IntegerField()
    user_listed_count = models.IntegerField()
    user_name = models.CharField(max_length=255)
    user_screen_name = models.CharField(max_length=255)
    user_statuses_count = models.IntegerField()
