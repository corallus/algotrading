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
                ('share', models.CharField(verbose_name='share', choices=[('YHOO', 'Yahoo'), ('IBM', 'IBM'), ('TSLA', 'Tesla'), ('ASML.AS', 'ASML')], max_length=31, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ShareDay',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('volume', models.PositiveIntegerField(verbose_name='volume')),
                ('adj_close', models.DecimalField(verbose_name='closing value', decimal_places=2, max_digits=12)),
                ('high', models.DecimalField(verbose_name='highest value', decimal_places=2, max_digits=12)),
                ('low', models.DecimalField(verbose_name='lowest value', decimal_places=2, max_digits=12)),
                ('date', models.DateTimeField(verbose_name='date')),
                ('close', models.DecimalField(verbose_name='close', decimal_places=2, max_digits=12)),
                ('open', models.DecimalField(verbose_name='open', decimal_places=2, max_digits=12)),
                ('share', models.ForeignKey(to='stock_retrieval.Share', verbose_name='share')),
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
                ('open', models.DecimalField(verbose_name='open', decimal_places=2, max_digits=12)),
                ('price', models.DecimalField(verbose_name='price', decimal_places=2, max_digits=12)),
                ('share', models.ForeignKey(to='stock_retrieval.Share', verbose_name='share')),
            ],
            options={
                'ordering': ['time'],
            },
        ),
    ]
