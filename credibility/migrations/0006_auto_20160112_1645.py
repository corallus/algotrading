# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('credibility', '0005_auto_20160112_1611'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sourcemodel',
            name='credibility_model',
        ),
        migrations.AddField(
            model_name='credibilitymodel',
            name='source',
            field=models.ForeignKey(to='credibility.SourceModel', null=True, related_name='credibility_model'),
        ),
    ]
