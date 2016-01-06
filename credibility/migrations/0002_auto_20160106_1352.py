# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('credibility', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='credibilitybasemodel',
            name='credibility',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='credibilitybasemodel',
            name='outgoing',
            field=models.ManyToManyField(related_name='incoming', to='credibility.CredibilityBaseModel'),
        ),
        migrations.AlterField(
            model_name='hits',
            name='auth',
            field=models.FloatField(default=1),
        ),
        migrations.AlterField(
            model_name='hits',
            name='hub',
            field=models.FloatField(default=1),
        ),
    ]
