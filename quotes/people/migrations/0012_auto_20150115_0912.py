# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0011_auto_20150115_0857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 15, 9, 12, 57, 502388), verbose_name=b'date published'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='updated_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 15, 9, 12, 57, 502419)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='quote',
            name='date',
            field=models.CharField(max_length=5),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='quote',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 15, 9, 12, 57, 503169), verbose_name=b'date published'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='quote',
            name='updated_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 15, 9, 12, 57, 503195)),
            preserve_default=True,
        ),
    ]
