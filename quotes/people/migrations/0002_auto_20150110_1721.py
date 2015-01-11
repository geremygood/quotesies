# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quote',
            name='votes',
        ),
        migrations.AddField(
            model_name='person',
            name='source',
            field=models.CharField(default='none', max_length=800),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='person',
            name='updated_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 10, 17, 21, 20, 339945)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='quote',
            name='quote_text',
            field=models.TextField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='quote',
            name='updated_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 10, 17, 21, 20, 340770)),
            preserve_default=True,
        ),
    ]
