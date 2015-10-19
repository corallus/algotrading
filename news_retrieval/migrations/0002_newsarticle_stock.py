# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news_retrieval', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsarticle',
            name='stock',
            field=models.CharField(default=2, max_length=127, choices=[('toyoya', 'toyota'), ('netflix', 'netflix'), ('asml', 'asml'), ('volkswagen', 'volkswagen')]),
            preserve_default=False,
        ),
    ]
