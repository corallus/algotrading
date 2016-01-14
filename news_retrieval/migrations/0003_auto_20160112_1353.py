# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news_retrieval', '0002_remove_newsarticle_stock'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='newsarticle',
            options={'ordering': ['document__published']},
        ),
        migrations.RemoveField(
            model_name='newsarticle',
            name='description',
        ),
        migrations.RemoveField(
            model_name='newsarticle',
            name='link',
        ),
        migrations.RemoveField(
            model_name='newsarticle',
            name='published',
        ),
        migrations.RemoveField(
            model_name='newsarticle',
            name='source',
        ),
        migrations.RemoveField(
            model_name='newsarticle',
            name='title',
        ),
    ]
