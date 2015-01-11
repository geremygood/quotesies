# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('person_name', models.CharField(max_length=200)),
                ('slug', models.SlugField()),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
                ('updated_date', models.DateTimeField(default=datetime.datetime(2015, 1, 7, 22, 31, 28, 635059))),
                ('wiki', models.URLField(verbose_name=b'Authors Wikipedia Page')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slug', models.SlugField()),
                ('quote_text', models.CharField(max_length=200)),
                ('votes', models.IntegerField(default=0)),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
                ('updated_date', models.DateTimeField(default=datetime.datetime(2015, 1, 7, 22, 31, 28, 635803))),
                ('topics', models.TextField()),
                ('person', models.ForeignKey(to='people.Person')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
