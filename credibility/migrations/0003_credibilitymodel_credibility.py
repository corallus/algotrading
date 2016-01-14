# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('credibility', '0002_sourcemodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='credibilitymodel',
            name='credibility',
            field=models.FloatField(default=1),
        ),
    ]
