# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0006_auto_20160112_1353'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='guid',
            field=models.CharField(verbose_name='guid', default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='document',
            name='type',
            field=models.CharField(default='na', choices=[('na', 'news article'), ('tw', 'tweet')], max_length=10),
            preserve_default=False,
        ),
    ]
