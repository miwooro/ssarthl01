# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2016-11-05 05:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tablemoney', '0010_tablemoney_pay_off'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monthlytotal',
            name='monthlytotal',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='tablemoney',
            name='totle_price',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
    ]
