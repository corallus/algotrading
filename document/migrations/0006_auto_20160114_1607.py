# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0005_document_source'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='similar',
            field=models.ForeignKey(default=None, to='document.Document', blank=True, null=True),
        ),
    ]
