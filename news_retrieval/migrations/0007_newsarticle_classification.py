# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news_retrieval', '0006_remove_newsarticle_summary'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsarticle',
            name='classification',
            field=models.CharField(max_length=127, verbose_name='classification', default=1),
            preserve_default=False,
        ),
    ]
