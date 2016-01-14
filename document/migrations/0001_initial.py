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
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('source', models.TextField(max_length=400)),
                ('published', models.DateTimeField(verbose_name=b'published')),
                ('title', models.CharField(max_length=200, verbose_name=b'title')),
                ('text', models.TextField(blank=True)),
                ('predicted_sentiment', models.CharField(max_length=127, null=True, verbose_name=b'predicted sentiment')),
                ('sentiment', models.CharField(max_length=127, null=True, verbose_name=b'sentiment')),
                ('credibility', models.IntegerField(default=1)),
                ('guid', models.CharField(max_length=200, verbose_name=b'guid')),
                ('type', models.CharField(max_length=10, choices=[(b'na', b'news article'), (b'tw', b'tweet')])),
            ],
            options={
                'ordering': ['published'],
            },
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
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
            field=models.ForeignKey(default=None, blank=True, to='document.Document', null=True),
        ),
    ]
