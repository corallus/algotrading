# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations, transaction
from social_retrieval.models import Tweet


def set_retweets_in_document(apps, schema_editor):
    with transaction.atomic():
        for tweet in Tweet.objects.all():
            if tweet.original:
                tweet.document.similar = tweet.original.document
                tweet.document.save()



class Migration(migrations.Migration):

    dependencies = [
        ('credibility', '0003_credibilitymodel_credibility'),
    ]

    operations = [
        migrations.RunPython(set_retweets_in_document)
    ]
