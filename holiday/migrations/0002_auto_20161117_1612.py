# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2016-11-17 08:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('holiday', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='holidaymonth',
            name='month',
            field=models.CharField(choices=[('一月', '一月'), ('二月', '二月'), ('三月', '三月'), ('四月', '四月'), ('五月', '五月'), ('六月', '六月'), ('七月', '七月'), ('八月', '八月'), ('九月', '九月'), ('十月', '十月'), ('十一月', '十一月'), ('十二月', '十二月')], max_length=20),
        ),
    ]
