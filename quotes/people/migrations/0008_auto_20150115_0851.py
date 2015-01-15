# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0007_auto_20150115_0851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 15, 8, 51, 41, 981998), verbose_name=b'date published'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='updated_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 15, 8, 51, 41, 982067)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='quote',
            name='date',
            field=models.DecimalField(default=0, max_digits=5, decimal_places=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='quote',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 15, 8, 51, 41, 983451), verbose_name=b'date published'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='quote',
            name='updated_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 15, 8, 51, 41, 983504)),
            preserve_default=True,
        ),
    ]
