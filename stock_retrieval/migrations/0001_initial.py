# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Share',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('share', models.CharField(unique=True, max_length=31, verbose_name='share', choices=[(b'YHOO', b'Yahoo'), (b'IBM', b'IBM'), (b'TSLA', b'Tesla'), (b'ASML.AS', b'ASML')])),
            ],
        ),
        migrations.CreateModel(
            name='ShareDay',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('volume', models.PositiveIntegerField(verbose_name='volume')),
                ('adj_close', models.DecimalField(verbose_name='closing value', max_digits=12, decimal_places=2)),
                ('high', models.DecimalField(verbose_name='highest value', max_digits=12, decimal_places=2)),
                ('low', models.DecimalField(verbose_name='lowest value', max_digits=12, decimal_places=2)),
                ('date', models.DateTimeField(verbose_name='date')),
                ('close', models.DecimalField(verbose_name='close', max_digits=12, decimal_places=2)),
                ('open', models.DecimalField(verbose_name='open', max_digits=12, decimal_places=2)),
                ('share', models.ForeignKey(verbose_name='share', to='stock_retrieval.Share')),
            ],
            options={
                'ordering': ['date'],
            },
        ),
        migrations.CreateModel(
            name='ShareValue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('volume', models.PositiveIntegerField(verbose_name='volume')),
                ('time', models.DateTimeField(verbose_name='date')),
                ('open', models.DecimalField(verbose_name='open', max_digits=12, decimal_places=2)),
                ('price', models.DecimalField(verbose_name='price', max_digits=12, decimal_places=2)),
                ('share', models.ForeignKey(verbose_name='share', to='stock_retrieval.Share')),
            ],
            options={
                'ordering': ['time'],
            },
        ),
    ]
