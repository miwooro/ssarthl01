# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2016-11-22 00:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tablemoney', '0057_auto_20161121_1416'),
    ]

    operations = [
        migrations.AddField(
            model_name='tablemoney',
            name='identify',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
