# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-17 13:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tablemoney', '0065_auto_20170217_2101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extratablemoney',
            name='identify',
            field=models.CharField(default=0, max_length=20),
        ),
    ]
