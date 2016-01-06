# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock_retrieval', '0006_auto_20160106_1319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shareday',
            name='date',
            field=models.DateTimeField(verbose_name='date'),
        ),
    ]
