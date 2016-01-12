# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0005_document_source'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='published',
            field=models.DateTimeField(verbose_name='published', default=datetime.datetime(2016, 1, 12, 13, 53, 35, 116572, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='document',
            name='title',
            field=models.CharField(verbose_name='title', max_length=200, default='a'),
            preserve_default=False,
        ),
    ]
