from django.db import models


class Link(models.Model):
    url = models.CharField(max_length=255)

    def __str__(self):
        return self.url


class BaseModel(models.Model):
    text = models.TextField()
    similar = models.ForeignKey('self', null=True, default=None)  # used for similar posts
    links = models.ManyToManyField(Link)  # TODO make sure all links are formatted the same


class Tweet(BaseModel):

    tweet_id = models.IntegerField()
    created_at = models.DateTimeField()
    favorite_count = models.IntegerField()
    in_reply_to_status_id = models.IntegerField(null=True)
    is_quote_status = models.BooleanField()
    retweet_count = models.IntegerField()
    original = models.ForeignKey('self', null=True)
    user_id = models.IntegerField()
    user_followers_count = models.IntegerField()
    user_favourites_count = models.IntegerField()
    user_friends_count = models.IntegerField()
    user_listed_count = models.IntegerField()
    user_name = models.CharField(max_length=255)
    user_screen_name = models.CharField(max_length=255)
    user_statuses_count = models.IntegerField()

    def __str__(self):
        return str(self.tweet_id)
