# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2016-11-05 05:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tablemoney', '0012_auto_20161105_0549'),
    ]

    operations = [
        migrations.AddField(
            model_name='month',
            name='month_total',
            field=models.IntegerField(default=0),
        ),
    ]
