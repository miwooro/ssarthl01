# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2016-11-20 07:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('holiday', '0010_auto_20161119_1529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='holiday',
            name='date',
            field=models.ManyToManyField(default='1', to='holiday.Date'),
        ),
    ]
