# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2016-11-06 07:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tablemoney', '0026_auto_20161106_0656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tablemoney',
            name='payee',
            field=models.ManyToManyField(to='userprofile.UserProfile'),
        ),
    ]
