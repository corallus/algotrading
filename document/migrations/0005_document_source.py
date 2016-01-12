# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0004_document_predicted_sentiment'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='source',
            field=models.TextField(max_length=400, default=''),
            preserve_default=False,
        ),
    ]
