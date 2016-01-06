# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='classification',
            field=models.CharField(verbose_name='classification', null=True, max_length=127),
        ),
        migrations.AlterField(
            model_name='document',
            name='text',
            field=models.TextField(blank=True),
        ),
    ]
