# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-18 00:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('train', '0010_remove_zhuditable_img3'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='zuxuntable',
            name='img3',
        ),
    ]
