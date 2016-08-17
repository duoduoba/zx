# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-08-17 22:13
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, unique=True, verbose_name='品牌名称')),
                ('logo', models.ImageField(blank=True, null=True, upload_to='logo/%Y-%m-%d/')),
                ('website_site', models.CharField(blank=True, max_length=100, null=True, verbose_name='网址')),
                ('description', models.CharField(blank=True, max_length=100, null=True, verbose_name='简要描述')),
                ('cited_times', models.PositiveIntegerField(default=0, verbose_name='引用次数')),
            ],
        ),
        migrations.CreateModel(
            name='BrandDataWithCityTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_cited_times', models.PositiveIntegerField(default=0)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jizhang.Brand', to_field='name')),
            ],
        ),
        migrations.CreateModel(
            name='BuyPlace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('latitude', models.FloatField(default=0.0)),
                ('longitude', models.FloatField(default=0.0)),
                ('latitudeE6', models.FloatField(default=0.0)),
                ('longitudeE6', models.FloatField(default=0.0)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('site', models.URLField(blank=True, null=True, verbose_name='web site')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True, verbose_name='分类名称')),
                ('description', models.CharField(blank=True, max_length=60, null=True, verbose_name='简要描述')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='jizhang.Category', to_field='name', verbose_name='上级分类')),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='城市名')),
                ('state', models.BooleanField(default=True, verbose_name='可用状态')),
            ],
        ),
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='RMB', max_length=14, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='DecorationCompany',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='装修公司名称')),
                ('addr', models.CharField(blank=True, max_length=30, null=True, verbose_name='公司地址')),
                ('phone', models.CharField(blank=True, max_length=30, null=True, verbose_name='电话')),
                ('site', models.CharField(blank=True, max_length=50, null=True, verbose_name='公司主页')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='city_company_set', to='jizhang.City', to_field='name', verbose_name='城市')),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='反馈')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, to_field='username', verbose_name='用户')),
            ],
        ),
        migrations.CreateModel(
            name='Province',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area_code', models.IntegerField(unique=True, verbose_name='省份编码')),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='省份名称')),
                ('state', models.BooleanField(default=True, verbose_name='可用状态')),
            ],
        ),
        migrations.CreateModel(
            name='ShopDataWithCityTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shop_cited_times', models.PositiveIntegerField(default=0)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jizhang.Brand', to_field='name')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jizhang.City', to_field='name')),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jizhang.BuyPlace', to_field='name')),
            ],
        ),
        migrations.CreateModel(
            name='SpendDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField()),
                ('note', models.TextField(blank=True, null=True)),
                ('image1', models.ImageField(blank=True, null=True, upload_to='detail/%Y-%m-%d/')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='detail/%Y-%m-%d/')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='detail/%Y-%m-%d/')),
                ('image4', models.ImageField(blank=True, null=True, upload_to='detail/%Y-%m-%d/')),
                ('created', models.DateTimeField(default='2016-01-01 00:00:00')),
                ('modified', models.DateTimeField(auto_now=True)),
                ('local_id', models.IntegerField(default=-1)),
                ('addr', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='jizhang.BuyPlace', to_field='name')),
                ('brand', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='jizhang.Brand', to_field='name')),
                ('city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='jizhang.City', to_field='name')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, to_field='username')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, unique=True, verbose_name='名称')),
                ('cited_times', models.PositiveIntegerField(default=0, verbose_name='引用次数')),
                ('average_price', models.FloatField(default=0.0, verbose_name='平均价格')),
                ('min_price', models.FloatField(default=0.0, verbose_name='最低价格')),
                ('max_price', models.FloatField(default=0.0, verbose_name='最高价格')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='category_tag_set', to='jizhang.Category', to_field='name', verbose_name='分类')),
                ('city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='city_tag_set', to='jizhang.City', to_field='name', verbose_name='城市')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nick_name', models.CharField(blank=True, max_length=30, null=True, verbose_name='昵称')),
                ('portrayal', models.ImageField(blank=True, null=True, upload_to='user/%Y-%m-%d/', verbose_name='头像')),
                ('signature', models.CharField(default='我的签名', max_length=30, verbose_name='签名')),
                ('house_area', models.FloatField(default=0.0, verbose_name='面积')),
                ('house_shape', models.CharField(blank=True, max_length=20, null=True, verbose_name='户型')),
                ('decoration_style', models.CharField(blank=True, max_length=30, null=True, verbose_name='装修风格')),
                ('budget', models.FloatField(default=0.0, max_length=10, verbose_name='预算')),
                ('company', models.CharField(blank=True, max_length=30, null=True, verbose_name='装修公司')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='city_user_set', to='jizhang.City', to_field='name', verbose_name='城市')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_profile', to=settings.AUTH_USER_MODEL, to_field='username')),
            ],
        ),
        migrations.AddField(
            model_name='spenddetail',
            name='tag',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='jizhang.Tag', to_field='name'),
        ),
        migrations.AddField(
            model_name='spenddetail',
            name='unit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='jizhang.Currency', to_field='name'),
        ),
        migrations.AddField(
            model_name='shopdatawithcitytag',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jizhang.Tag', to_field='name'),
        ),
        migrations.AddField(
            model_name='city',
            name='province',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='province_city_set', to='jizhang.Province', to_field='name', verbose_name='所在省份'),
        ),
        migrations.AddField(
            model_name='branddatawithcitytag',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jizhang.City', to_field='name'),
        ),
        migrations.AddField(
            model_name='branddatawithcitytag',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jizhang.Tag', to_field='name'),
        ),
    ]
