# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news_retrieval', '0003_auto_20151020_1518'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newsarticle',
            name='google_id',
        ),
        migrations.AddField(
            model_name='newsarticle',
            name='enclosure',
            field=models.CharField(default=1, max_length=400, verbose_name='enclosure'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='newsarticle',
            name='guid',
            field=models.CharField(default=1, max_length=200, verbose_name='guid'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='newsarticle',
            name='source',
            field=models.CharField(default=1, max_length=400, verbose_name='source'),
            preserve_default=False,
        ),
    ]
