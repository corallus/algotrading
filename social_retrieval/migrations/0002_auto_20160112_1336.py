# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social_retrieval', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tweet',
            options={'ordering': ['document__share', 'created_at']},
        ),
        migrations.AlterField(
            model_name='tweet',
            name='document',
            field=models.OneToOneField(to='document.Document', related_name='tweet'),
        ),
    ]
