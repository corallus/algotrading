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
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('share', models.CharField(choices=[('YHOO', 'Yahoo'), ('IBM', 'IBM'), ('TSLA', 'Tesla'), ('ASML.AS', 'ASML')], verbose_name='share', max_length=31, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ShareDay',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('volume', models.PositiveIntegerField(verbose_name='volume')),
                ('adj_close', models.DecimalField(max_digits=12, verbose_name='closing value', decimal_places=2)),
                ('high', models.DecimalField(max_digits=12, verbose_name='highest value', decimal_places=2)),
                ('low', models.DecimalField(max_digits=12, verbose_name='lowest value', decimal_places=2)),
                ('date', models.DateTimeField(verbose_name='date')),
                ('close', models.DecimalField(max_digits=12, verbose_name='close', decimal_places=2)),
                ('open', models.DecimalField(max_digits=12, verbose_name='open', decimal_places=2)),
                ('share', models.ForeignKey(verbose_name='share', to='stock_retrieval.Share')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]
