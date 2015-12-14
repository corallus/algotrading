# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock_retrieval', '0002_stockprice'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='slug',
            field=models.SlugField(unique=True, default=1),
            preserve_default=False,
        ),
    ]
