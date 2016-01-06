# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock_retrieval', '0005_auto_20151119_1439'),
    ]

    operations = [
        migrations.AlterField(
            model_name='share',
            name='share',
            field=models.CharField(max_length=31, choices=[('YHOO', 'Yahoo'), ('IBM', 'IBM'), ('TSLA', 'Tesla'), ('ASML.AS', 'ASML')], verbose_name='share', unique=True),
        ),
    ]
