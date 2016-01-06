# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social_retrieval', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BaseModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('url', models.CharField(max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='tweet',
            name='id',
        ),
        migrations.RemoveField(
            model_name='tweet',
            name='text',
        ),
        migrations.AddField(
            model_name='basemodel',
            name='links',
            field=models.ManyToManyField(to='social_retrieval.Link'),
        ),
        migrations.AddField(
            model_name='basemodel',
            name='similar',
            field=models.ForeignKey(default=None, to='social_retrieval.BaseModel', null=True),
        ),
        migrations.AddField(
            model_name='tweet',
            name='basemodel_ptr',
            field=models.OneToOneField(to='social_retrieval.BaseModel', auto_created=True, primary_key=True, serialize=False, default=1, parent_link=True),
            preserve_default=False,
        ),
    ]
