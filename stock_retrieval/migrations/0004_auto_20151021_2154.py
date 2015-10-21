# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock_retrieval', '0003_stock_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='stockprice',
            options={'ordering': ['stock']},
        ),
        migrations.AlterField(
            model_name='stockprice',
            name='price',
            field=models.FloatField(verbose_name='price'),
        ),
    ]
