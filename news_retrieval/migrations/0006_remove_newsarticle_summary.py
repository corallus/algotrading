# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news_retrieval', '0005_newsarticle_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newsarticle',
            name='summary',
        ),
    ]
