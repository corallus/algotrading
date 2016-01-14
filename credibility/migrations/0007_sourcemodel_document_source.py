# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('credibility', '0006_auto_20160112_1645'),
    ]

    operations = [
        migrations.AddField(
            model_name='sourcemodel',
            name='document_source',
            field=models.TextField(max_length=400, default=''),
            preserve_default=False,
        ),
    ]
