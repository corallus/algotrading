# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CredibilityModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hub', models.FloatField(default=1)),
                ('auth', models.FloatField(default=0)),
                ('source_score', models.FloatField(default=0)),
                ('credibility', models.FloatField(default=1)),
                ('document', models.OneToOneField(null=True, to='document.Document')),
                ('outgoing', models.ManyToManyField(to='credibility.CredibilityModel', related_name='incoming')),
            ],
        ),
        migrations.CreateModel(
            name='SourceModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('document_source', models.TextField(max_length=400)),
                ('source_correct', models.FloatField(default=0)),
                ('total', models.FloatField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='credibilitymodel',
            name='source',
            field=models.ForeignKey(null=True, to='credibility.SourceModel', related_name='credibility_models'),
        ),
    ]
