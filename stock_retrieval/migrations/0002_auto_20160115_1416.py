# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock_retrieval', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sharevalue',
            name='open',
            field=models.DecimalField(max_digits=12, decimal_places=2, verbose_name='open', null=True),
        ),
    ]
