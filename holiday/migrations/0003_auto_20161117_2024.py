# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2016-11-17 12:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('holiday', '0002_auto_20161117_1612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='holiday',
            name='date',
            field=models.ManyToManyField(blank=True, null=True, to='holiday.Date'),
        ),
    ]
