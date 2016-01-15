# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social_retrieval', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='favorite_count',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='in_reply_to_status_id',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='tweet_id',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='user_favourites_count',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='user_followers_count',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='user_friends_count',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='user_id',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='user_listed_count',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='user_statuses_count',
            field=models.BigIntegerField(),
        ),
    ]
