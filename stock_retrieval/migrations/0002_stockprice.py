# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock_retrieval', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StockPrice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('published', models.DateTimeField(auto_now_add=True, verbose_name='published')),
                ('price', models.IntegerField(verbose_name='price')),
                ('stock', models.ForeignKey(verbose_name='stock', to='stock_retrieval.Stock')),
            ],
        ),
    ]
