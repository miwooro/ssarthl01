# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2016-12-06 01:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('holiday', '0027_auto_20161206_0953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='holidaymonth',
            name='month',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12')], max_length=20),
        ),
    ]
