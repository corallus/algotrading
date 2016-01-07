import json
from django.conf import settings
from django.views.generic import ListView
import oauth2
from time import strptime, strftime

from document.models import Link, Document
from social_retrieval.models import Tweet
from stock_retrieval.models import Share
from .management.commands.fetch_tweets import Command


class TwitterView(ListView):
    template_name = 'social_retrieval/twitter.html'
    model = Tweet


class TwitterManualView(TwitterView):

    def get(self, *args, **kwargs):
        command = Command()
        command.handle()

        return super(TwitterManualView, self).get(*args, **kwargs)
