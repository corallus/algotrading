# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social_retrieval', '0003_tweet_original'),
    ]

    operations = [
        migrations.CreateModel(
            name='CredibilityBaseModel',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('credibility', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='HITS',
            fields=[
                ('credibilitybasemodel_ptr', models.OneToOneField(parent_link=True, primary_key=True, serialize=False, auto_created=True, to='credibility.CredibilityBaseModel')),
                ('hub', models.IntegerField(default=1)),
                ('auth', models.IntegerField(default=1)),
            ],
            bases=('credibility.credibilitybasemodel',),
        ),
        migrations.AddField(
            model_name='credibilitybasemodel',
            name='outgoing',
            field=models.ManyToManyField(related_name='outgoing_rel_+', to='credibility.CredibilityBaseModel'),
        ),
        migrations.AddField(
            model_name='credibilitybasemodel',
            name='tweet',
            field=models.ForeignKey(to='social_retrieval.Tweet', null=True),
        ),
    ]
