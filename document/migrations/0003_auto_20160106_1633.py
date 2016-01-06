# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0002_auto_20160106_1631'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='classification',
        ),
        migrations.AddField(
            model_name='document',
            name='sentiment',
            field=models.CharField(verbose_name='sentiment', max_length=127, null=True),
        ),
    ]
