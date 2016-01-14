# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news_retrieval', '0003_auto_20160112_1353'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newsarticle',
            name='document',
        ),
        migrations.DeleteModel(
            name='NewsArticle',
        ),
    ]
