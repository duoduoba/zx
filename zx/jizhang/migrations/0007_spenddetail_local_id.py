# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-14 22:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jizhang', '0006_auto_20160413_1923'),
    ]

    operations = [
        migrations.AddField(
            model_name='spenddetail',
            name='local_id',
            field=models.IntegerField(default=-1),
        ),
    ]
