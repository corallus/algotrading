# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news_retrieval', '0002_newsarticle_stock'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='newsarticle',
            options={'ordering': ['published']},
        ),
        migrations.AddField(
            model_name='newsarticle',
            name='description',
            field=models.TextField(verbose_name='description', default=2),
            preserve_default=False,
        ),
    ]
