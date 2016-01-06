# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsArticle',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('guid', models.CharField(verbose_name='guid', max_length=200)),
                ('link', models.CharField(verbose_name='link', max_length=400)),
                ('source', models.CharField(verbose_name='source', max_length=400)),
                ('published', models.DateTimeField(verbose_name='published')),
                ('description', models.TextField(verbose_name='description')),
                ('title', models.CharField(verbose_name='title', max_length=200)),
                ('stock', models.CharField(choices=[('YHOO', 'Yahoo'), ('IBM', 'IBM'), ('TSLA', 'Tesla'), ('ASML.AS', 'ASML')], max_length=127)),
                ('enclosure', models.CharField(verbose_name='enclosure', max_length=400)),
                ('category', models.CharField(verbose_name='category', max_length=127)),
                ('document', models.OneToOneField(to='document.Document')),
            ],
            options={
                'ordering': ['published'],
            },
        ),
    ]
