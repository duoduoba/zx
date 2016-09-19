# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-16 23:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jizhang', '0005_remove_buyplacedatawithcity_buy_city'),
    ]

    operations = [
        migrations.CreateModel(
            name='TagDataWithoutCity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cited_times', models.PositiveIntegerField(default=1, verbose_name='引用次数')),
                ('average_price', models.FloatField(default=0.0, verbose_name='平均价格')),
                ('min_price', models.FloatField(default=0.0, verbose_name='最低价格')),
                ('max_price', models.FloatField(default=0.0, verbose_name='最高价格')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jizhang.Tag', to_field='name', verbose_name='标签名称')),
            ],
        ),
    ]