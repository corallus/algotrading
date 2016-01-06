# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CredibilityModel',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('hub', models.FloatField(default=1)),
                ('auth', models.FloatField(default=1)),
                ('document', models.OneToOneField(null=True, to='document.Document')),
                ('outgoing', models.ManyToManyField(related_name='incoming', to='credibility.CredibilityModel')),
            ],
        ),
    ]
