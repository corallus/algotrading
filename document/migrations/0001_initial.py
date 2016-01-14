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
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('source', models.TextField(max_length=400)),
                ('published', models.DateTimeField(verbose_name='published')),
                ('title', models.CharField(max_length=200, verbose_name='title')),
                ('text', models.TextField(blank=True)),
                ('predicted_sentiment', models.CharField(null=True, max_length=127, verbose_name='predicted sentiment')),
                ('sentiment', models.CharField(null=True, max_length=127, verbose_name='sentiment')),
                ('credibility', models.IntegerField(default=1)),
                ('guid', models.CharField(max_length=200, verbose_name='guid')),
                ('type', models.CharField(choices=[('na', 'news article'), ('tw', 'tweet')], max_length=10)),
            ],
            options={
                'ordering': ['published'],
            },
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
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
            field=models.ForeignKey(to='document.Document', default=None, null=True, blank=True),
        ),
    ]
