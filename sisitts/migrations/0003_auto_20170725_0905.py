# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-25 06:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sisitts', '0002_sisit_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sisit',
            name='likes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='sisit',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
