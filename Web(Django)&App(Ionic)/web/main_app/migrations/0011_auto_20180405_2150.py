# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-04-05 21:50
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0010_auto_20180405_1931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addbook',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2018, 4, 5, 21, 50, 26, 60682), verbose_name='Date'),
        ),
    ]
