# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social_retrieval', '0002_auto_20151116_1623'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='original',
            field=models.ForeignKey(to='social_retrieval.Tweet', null=True),
        ),
    ]
