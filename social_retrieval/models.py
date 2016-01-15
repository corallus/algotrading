from django.db import models

from document.models import Document


class Tweet(models.Model):
    document = models.OneToOneField(Document, related_name='tweet')
    tweet_id = models.BigIntegerField()
    created_at = models.DateTimeField()
    favorite_count = models.BigIntegerField()
    in_reply_to_status_id = models.BigIntegerField(null=True)
    is_quote_status = models.BooleanField()
    retweet_count = models.IntegerField()
    original = models.ForeignKey('self', null=True)
    user_id = models.BigIntegerField()
    user_followers_count = models.BigIntegerField()
    user_favourites_count = models.BigIntegerField()
    user_friends_count = models.BigIntegerField()
    user_listed_count = models.BigIntegerField()
    user_name = models.CharField(max_length=255)
    user_screen_name = models.CharField(max_length=255)
    user_statuses_count = models.BigIntegerField()

    def __str__(self):
        return str(self.tweet_id)

    class Meta:
        ordering = ['document__share', 'created_at']
