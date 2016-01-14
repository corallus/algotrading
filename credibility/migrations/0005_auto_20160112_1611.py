# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('credibility', '0004_auto_20160112_1412'),
    ]

    operations = [
        migrations.AddField(
            model_name='credibilitymodel',
            name='source_score',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='sourcemodel',
            name='source_correct',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='sourcemodel',
            name='total',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='credibilitymodel',
            name='auth',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='credibilitymodel',
            name='hub',
            field=models.FloatField(default=0),
        ),
    ]
