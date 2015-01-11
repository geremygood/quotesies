# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0002_auto_20150110_1721'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='source',
        ),
        migrations.AddField(
            model_name='quote',
            name='source',
            field=models.TextField(default='none'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='person',
            name='updated_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 10, 17, 24, 31, 657144)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='quote',
            name='topics',
            field=models.CharField(max_length=200),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='quote',
            name='updated_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 10, 17, 24, 31, 657918)),
            preserve_default=True,
        ),
    ]
