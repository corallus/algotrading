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
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('share', models.CharField(max_length=31, verbose_name='share', unique=True, choices=[('YHOO', 'Yahoo'), ('IBM', 'IBM'), ('TSLA', 'Tesla'), ('ASML.AS', 'ASML')])),
            ],
        ),
        migrations.CreateModel(
            name='ShareDay',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('volume', models.PositiveIntegerField(verbose_name='volume')),
                ('adj_close', models.DecimalField(max_digits=12, decimal_places=2, verbose_name='closing value')),
                ('high', models.DecimalField(max_digits=12, decimal_places=2, verbose_name='highest value')),
                ('low', models.DecimalField(max_digits=12, decimal_places=2, verbose_name='lowest value')),
                ('date', models.DateTimeField(verbose_name='date')),
                ('close', models.DecimalField(max_digits=12, decimal_places=2, verbose_name='close')),
                ('open', models.DecimalField(max_digits=12, decimal_places=2, verbose_name='open')),
                ('share', models.ForeignKey(to='stock_retrieval.Share', verbose_name='share')),
            ],
            options={
                'ordering': ['date'],
            },
        ),
        migrations.CreateModel(
            name='ShareValue',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('volume', models.PositiveIntegerField(verbose_name='volume')),
                ('time', models.DateTimeField(verbose_name='date')),
                ('open', models.DecimalField(max_digits=12, decimal_places=2, verbose_name='open')),
                ('price', models.DecimalField(max_digits=12, decimal_places=2, verbose_name='price')),
                ('share', models.ForeignKey(to='stock_retrieval.Share', verbose_name='share')),
            ],
            options={
                'ordering': ['time'],
            },
        ),
    ]
