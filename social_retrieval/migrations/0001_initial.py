# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tweet_id', models.IntegerField()),
                ('created_at', models.DateTimeField()),
                ('favorite_count', models.IntegerField()),
                ('in_reply_to_status_id', models.IntegerField(null=True)),
                ('is_quote_status', models.BooleanField()),
                ('retweet_count', models.IntegerField()),
                ('user_id', models.IntegerField()),
                ('user_followers_count', models.IntegerField()),
                ('user_favourites_count', models.IntegerField()),
                ('user_friends_count', models.IntegerField()),
                ('user_listed_count', models.IntegerField()),
                ('user_name', models.CharField(max_length=255)),
                ('user_screen_name', models.CharField(max_length=255)),
                ('user_statuses_count', models.IntegerField()),
                ('document', models.OneToOneField(to='document.Document', related_name='tweet')),
                ('original', models.ForeignKey(to='social_retrieval.Tweet', null=True)),
            ],
            options={
                'ordering': ['document__share', 'created_at'],
            },
        ),
    ]
