# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-12-03 22:32
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jizhang', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='uuid',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='装修攻略正文'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(default='title', max_length=50, verbose_name='攻略标题'),
        ),
    ]
