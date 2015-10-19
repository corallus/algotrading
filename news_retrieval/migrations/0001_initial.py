# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsArticle',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('google_id', models.CharField(verbose_name='id', max_length=200)),
                ('link', models.CharField(verbose_name='link', max_length=400)),
                ('published', models.DateTimeField(verbose_name='published')),
                ('summary', models.TextField(verbose_name='summary')),
                ('title', models.CharField(verbose_name='title', max_length=200)),
            ],
        ),
    ]
