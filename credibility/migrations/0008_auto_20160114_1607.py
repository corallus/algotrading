# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('credibility', '0007_sourcemodel_document_source'),
    ]

    operations = [
        migrations.AlterField(
            model_name='credibilitymodel',
            name='source',
            field=models.ForeignKey(to='credibility.SourceModel', related_name='credibility_models', null=True),
        ),
    ]
