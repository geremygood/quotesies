# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0004_auto_20150110_1729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 10, 17, 29, 47, 273735), verbose_name=b'date published'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='updated_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 10, 17, 29, 47, 273766)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='quote',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 10, 17, 29, 47, 274464), verbose_name=b'date published'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='quote',
            name='updated_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 10, 17, 29, 47, 274491)),
            preserve_default=True,
        ),
    ]
