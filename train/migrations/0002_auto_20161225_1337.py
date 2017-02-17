# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2016-12-25 05:37
from __future__ import unicode_literals

from django.db import migrations, models
import train.models


class Migration(migrations.Migration):

    dependencies = [
        ('train', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='zuxuntable',
            name='img2',
            field=models.FileField(default=1, upload_to=train.models.upload_location),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='zuxuntable',
            name='img3',
            field=models.FileField(blank=True, upload_to=train.models.upload_location),
        ),
        migrations.AlterField(
            model_name='zuxuntable',
            name='img',
            field=models.FileField(upload_to=train.models.upload_location),
        ),
    ]