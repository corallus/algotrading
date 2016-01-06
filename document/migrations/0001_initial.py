# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock_retrieval', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('text', models.TextField()),
                ('classification', models.CharField(verbose_name='classification', max_length=127)),
                ('credibility', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('url', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='document',
            name='links',
            field=models.ManyToManyField(to='document.Link'),
        ),
        migrations.AddField(
            model_name='document',
            name='share',
            field=models.ForeignKey(to='stock_retrieval.Share'),
        ),
        migrations.AddField(
            model_name='document',
            name='similar',
            field=models.ForeignKey(null=True, default=None, to='document.Document'),
        ),
    ]
