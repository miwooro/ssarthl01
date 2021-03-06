# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2016-11-13 07:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tablemoney', '0040_auto_20161113_1458'),
    ]

    operations = [
        migrations.CreateModel(
            name='MemberDayPrice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='SubstituteDayPrice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterField(
            model_name='tablemoney',
            name='member_day_price',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='tablemoney.MemberDayPrice'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tablemoney',
            name='substitute_day_price',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='tablemoney.SubstituteDayPrice'),
            preserve_default=False,
        ),
    ]
