# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-04-06 00:03
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0013_auto_20180405_2357'),
    ]

    operations = [
        migrations.AddField(
            model_name='borrowbook',
            name='returned_time',
            field=models.TimeField(blank=True, null=True, verbose_name='Returned time'),
        ),
        migrations.AlterField(
            model_name='addbook',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2018, 4, 6, 0, 3, 48, 407156), verbose_name='Date'),
        ),
    ]
