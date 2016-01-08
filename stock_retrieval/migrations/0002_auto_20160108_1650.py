# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock_retrieval', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShareValue',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
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
        migrations.AlterModelOptions(
            name='shareday',
            options={'ordering': ['date']},
        ),
    ]
