# coding：utf-8

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_delete
from django.dispatch import receiver
from jizhang.log.logger import logger


class Province(models.Model):
    area_code = models.IntegerField(verbose_name='省份编码', unique=True)
    name = models.CharField(verbose_name='省份名称', unique=True, max_length=30)
    state = models.BooleanField(verbose_name='可用状态', default=True)

    def __str__(self):
        return self.name


class City(models.Model):
    # province = models.ForeignKey(Province, to_field='name', related_name='province_city_set', verbose_name='所在省份')
    name = models.CharField(verbose_name='城市名', max_length=30, unique=True)
    # state = models.BooleanField(verbose_name='可用状态', default=True)

    def __str__(self):
        return self.name


class DecorationCompany(models.Model):
    city = models.ForeignKey(City, to_field='name', related_name='city_company_set', verbose_name='城市')
    name = models.CharField(verbose_name='装修公司名称', max_length=30, unique=True)
    addr = models.CharField(verbose_name='公司地址', max_length=30, null=True, blank=True)
    phone = models.CharField(verbose_name='电话', max_length=30, null=True, blank=True)
    site = models.CharField(verbose_name='公司主页', max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    user = models.OneToOneField(User, to_field='username', related_name='user_profile', verbose_name='用户名')
    nick_name = models.CharField(verbose_name='昵称', max_length=30, null=True, blank=True)
    city = models.ForeignKey(City, to_field='name', related_name='city_user_set', null=True, blank=True, verbose_name='城市')
    portrayal = models.ImageField(verbose_name='头像', upload_to='user/%Y-%m-%d/', blank=True, null=True)
    signature = models.CharField(verbose_name='签名', max_length=30, default='我的签名')
    house_area = models.CharField(verbose_name='面积', max_length=30, default='0.0')
    house_shape = models.CharField(verbose_name='户型', max_length=20, blank=True, null=True)
    decoration_style = models.CharField(verbose_name='装修风格', max_length=30, blank=True, null=True)
    budget = models.CharField(verbose_name='预算', max_length=10,  blank=True, null=True)
    company = models.CharField(verbose_name='装修公司', max_length=30, null=True, blank=True)

    def __str__(self):
        return '_'.join((self.user.username, self.city.name))


class Category(models.Model):
    name = models.CharField(verbose_name='分类名称', max_length=20, unique=True)
    parent = models.ForeignKey('self', to_field='name', null=True, blank=True, verbose_name='上级分类')
    description = models.CharField(max_length=60, null=True, blank=True, verbose_name='简要描述')

    def __str__(self):
        return self.name


class Currency(models.Model):
    name = models.CharField(max_length=14, unique=True, default='RMB')

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(verbose_name='品牌名称', max_length=40, unique=True)
    logo = models.ImageField(upload_to='logo/%Y-%m-%d/', null=True, blank=True)
    website_site = models.CharField(verbose_name='网址', max_length=100, null=True, blank=True)
    description = models.CharField(verbose_name='简要描述', max_length=100, null=True, blank=True)
    cited_times = models.PositiveIntegerField(verbose_name='引用次数', default=0)

    def __str__(self):
        return self.name


class Tag(models.Model):
    category = models.ForeignKey(Category, to_field='name', related_name='category_tag_set', null=True, blank=True, verbose_name='分类')
    name = models.CharField(max_length=40, unique=True, verbose_name='名称')

    def __str__(self):
        return self.name


class BuyPlace(models.Model):
    place_area = models.CharField(max_length=20, null=True, blank=True, verbose_name='所在购买城市')
    place_name = models.CharField(max_length=50, verbose_name='购买地点')
    latitude = models.FloatField(default=0.0, null=True, blank=True, verbose_name='经度')
    longitude = models.FloatField(default=0.0, null=True, blank=True, verbose_name='维度')
    latitudeE6 = models.FloatField(default=0.0, null=True, blank=True, verbose_name='经度6')
    longitudeE6 = models.FloatField(default=0.0, null=True, blank=True, verbose_name='维度6')
    address = models.CharField(max_length=100, null=True, blank=True, verbose_name='详细地址')
    phone = models.CharField(max_length=20, null=True, blank=True, verbose_name='电话')
    site = models.URLField(null=True, blank=True, verbose_name='网址')

    def __str__(self):
        return self.place_name


class SpendDetail(models.Model):
    owner = models.ForeignKey(User, to_field='username', verbose_name='用户名')
    price = models.FloatField(verbose_name='价格')
    unit = models.ForeignKey(Currency, to_field='name', null=True, blank=True, verbose_name='单位')

    tag = models.ForeignKey(Tag, to_field='name', null=True, blank=True, verbose_name='标签')
    brand = models.ForeignKey(Brand, to_field='name', null=True, blank=True, verbose_name='品牌')
    buy_place = models.ForeignKey(BuyPlace, null=True, blank=True, verbose_name='购买地点')

    note = models.TextField(null=True, blank=True, verbose_name='备注')
    image1 = models.ImageField(upload_to='detail/%Y-%m-%d/', blank=True, null=True)
    image2 = models.ImageField(upload_to='detail/%Y-%m-%d/', blank=True, null=True)
    image3 = models.ImageField(upload_to='detail/%Y-%m-%d/', blank=True, null=True)
    image4 = models.ImageField(upload_to='detail/%Y-%m-%d/', blank=True, null=True)

    created = models.DateTimeField(default='2016-01-01 00:00:00', verbose_name='创建时间')
    modified = models.DateTimeField(auto_now=True, verbose_name='更新日期')
    local_id = models.IntegerField(default=-1, verbose_name='客户端ID')

    def __str__(self):
        return str(self.price)
    #     return str(self.price) + '_' + self.tag + '_' + self.brand


@receiver(post_delete, sender=SpendDetail)
def photo_post_delete_handler(sender, **kwargs):
    detail = kwargs['instance']
    logger.info(detail)
    for index in range(1, 5):
        image_name = 'image' + str(index)
        logger.info(image_name)
        image_path = detail.__dict__[image_name]
        image_path = image_path.replace('/', '\\')
        import os
        from zx.settings import MEDIA_ROOT
        image_path = MEDIA_ROOT + '\\' + image_path
        logger.info(image_path)
        if os.path.isfile(image_path):
            os.remove(image_path)


#############################################################
# 根据用户的“记一笔”数据，统计完成
###########################################################

class TagDataWithoutCity(models.Model):
    '''
    不以城市分类，根据全部记录和当前价格，给出推荐的标签
    '''
    tag = models.ForeignKey(Tag, to_field='name', verbose_name='标签名称')
    cited_times = models.PositiveIntegerField(default=1, verbose_name='引用次数')
    average_price = models.FloatField(default=0.0, verbose_name='平均价格')
    min_price = models.FloatField(default=0.0, verbose_name='最低价格')
    max_price = models.FloatField(default=0.0, verbose_name='最高价格')

    def __str__(self):
        return self.tag.name + " cited times:" + str(self.cited_times)


class TagDataWithCity(models.Model):
    '''
    每个城市里面，根据价格，给出推荐的标签
    '''
    tag = models.ForeignKey(Tag, to_field='name', verbose_name='标签名称')
    city = models.ForeignKey(City, to_field='name', verbose_name='城市')
    cited_times = models.PositiveIntegerField(default=1, verbose_name='引用次数')
    average_price = models.FloatField(default=0.0, verbose_name='平均价格')
    min_price = models.FloatField(default=0.0, verbose_name='最低价格')
    max_price = models.FloatField(default=0.0, verbose_name='最高价格')

    class Meta:
        unique_together = ("tag", "city")

    def __str__(self):
        return self.tag.name + " city:" + self.city.name + " cited times:" + str(self.cited_times)


class BrandDataWithCityTag(models.Model):
    """
    根据城市和标签，给出推荐的品牌
    """
    city = models.ForeignKey(City, to_field='name', verbose_name='城市')
    tag = models.ForeignKey(Tag, to_field='name', verbose_name='标签')
    brand = models.ForeignKey(Brand, to_field='name', verbose_name='品牌')
    cited_times = models.PositiveIntegerField(default=1, verbose_name='引用次数')

    class Meta:
        unique_together = ("city", "tag", "brand")

    def __str__(self):
        return '_'.join((self.city.name, self.tag.name, self.brand.name, str(self.cited_times)))


class BuyPlaceDataWithCity(models.Model):
    '''
    根据每个城市，给出常见的购买地点
    '''
    city = models.ForeignKey(City, to_field='name', verbose_name='所在城市')
    # buy_place_area = models.CharField(max_length=30, verbose_name='城市')
    buy_place_name = models.CharField(max_length=50, verbose_name='购买地点')
    cited_times = models.PositiveIntegerField(default=1, verbose_name='引用次数')

    class Meta:
        unique_together = (("city", "buy_place_name"),)

    def __str__(self):
        return '_'.join((self.city.name, self.buy_place_name, str(self.cited_times)))


class Feedback(models.Model):
    owner = models.ForeignKey(User, to_field='username', verbose_name='用户')
    content = models.TextField(verbose_name='反馈')
    created = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    def __str__(self):
        return self.owner.username
