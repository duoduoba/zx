# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-12-04 18:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jizhang', '0002_auto_20161203_2232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='uuid',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]
