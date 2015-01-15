# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0008_auto_20150115_0851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 15, 8, 52, 12, 396818), verbose_name=b'date published'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='updated_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 15, 8, 52, 12, 396861)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='quote',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 15, 8, 52, 12, 397712), verbose_name=b'date published'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='quote',
            name='updated_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 15, 8, 52, 12, 397744)),
            preserve_default=True,
        ),
    ]
