# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock_retrieval', '0004_auto_20151021_2154'),
    ]

    operations = [
        migrations.CreateModel(
            name='Share',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('share', models.CharField(verbose_name='share', choices=[('YHOO', 'Yahoo'), ('IBM', 'IBM'), ('TSLA', 'Tesla'), ('ASML.AS', 'ASML')], max_length=31)),
            ],
        ),
        migrations.CreateModel(
            name='ShareDay',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('volume', models.PositiveIntegerField(verbose_name='volume')),
                ('adj_close', models.DecimalField(decimal_places=2, max_digits=12, verbose_name='closing value')),
                ('high', models.DecimalField(decimal_places=2, max_digits=12, verbose_name='highest value')),
                ('low', models.DecimalField(decimal_places=2, max_digits=12, verbose_name='lowest value')),
                ('date', models.DateField(verbose_name='date')),
                ('close', models.DecimalField(decimal_places=2, max_digits=12, verbose_name='close')),
                ('open', models.DecimalField(decimal_places=2, max_digits=12, verbose_name='open')),
                ('share', models.ForeignKey(to='stock_retrieval.Share', verbose_name='share')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.RemoveField(
            model_name='stockprice',
            name='stock',
        ),
        migrations.DeleteModel(
            name='Stock',
        ),
        migrations.DeleteModel(
            name='StockPrice',
        ),
    ]
