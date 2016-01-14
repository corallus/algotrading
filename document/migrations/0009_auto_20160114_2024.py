# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0008_merge'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='document',
            options={'ordering': ['published']},
        ),
    ]
