# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news_retrieval', '0004_auto_20151020_1523'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsarticle',
            name='category',
            field=models.CharField(max_length=127, verbose_name='category', default=1),
            preserve_default=False,
        ),
    ]
