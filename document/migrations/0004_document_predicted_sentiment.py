# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0003_auto_20160106_1633'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='predicted_sentiment',
            field=models.CharField(verbose_name='predicted sentiment', max_length=127, null=True),
        ),
    ]
