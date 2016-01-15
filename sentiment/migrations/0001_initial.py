# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock_retrieval', '0002_auto_20160115_1416'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prediction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('prediction', models.IntegerField(verbose_name='prediction')),
                ('share', models.ForeignKey(to='stock_retrieval.Share')),
            ],
        ),
    ]
