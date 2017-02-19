# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-18 09:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('holiday', '0038_auto_20170218_1549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='holidayfromdocx',
            name='month',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='holiday.HolidayMonth'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='holidayfromdocx',
            name='year',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]
