# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-17 13:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0012_userprofile_eat'),
        ('tablemoney', '0066_auto_20170217_2104'),
    ]

    operations = [
        migrations.AddField(
            model_name='extratablemoney',
            name='note',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='extratablemoney',
            name='pay_date',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='extratablemoney',
            name='pay_off',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='extratablemoney',
            name='payee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='userprofile.Payee'),
        ),
    ]
