# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-10-23 23:12
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jizhang', '0002_article'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appversion',
            name='version',
        ),
        migrations.AddField(
            model_name='appversion',
            name='cover_end_data',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='appversion',
            name='cover_start_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='appversion',
            name='cover_update',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='appversion',
            name='cover_url',
            field=models.FileField(default=datetime.datetime(2016, 10, 23, 23, 12, 3, 613934), upload_to='Cover', verbose_name='封面'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='appversion',
            name='version_code',
            field=models.PositiveIntegerField(default=1, verbose_name='版本号'),
        ),
        migrations.AddField(
            model_name='appversion',
            name='version_name',
            field=models.CharField(default=1.12, max_length=10, verbose_name='版本名'),
            preserve_default=False,
        ),
    ]