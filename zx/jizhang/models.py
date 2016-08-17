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
    province = models.ForeignKey(Province, to_field='name', related_name='province_city_set', verbose_name='所在省份')
    name = models.CharField(verbose_name='城市名', max_length=30, unique=True)
    state = models.BooleanField(verbose_name='可用状态', default=True)

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
    user = models.OneToOneField(User, to_field='username', related_name='user_profile')
    nick_name = models.CharField(verbose_name='昵称', max_length=30, null=True, blank=True)
    city = models.ForeignKey(City, to_field='name', related_name='city_user_set', verbose_name='城市')
    portrayal = models.ImageField(verbose_name='头像', upload_to='user/%Y-%m-%d/', blank=True, null=True)
    signature = models.CharField(verbose_name='签名', max_length=30, default='我的签名')
    house_area = models.FloatField(verbose_name='面积', default=0.0)
    house_shape = models.CharField(verbose_name='户型', max_length=20, blank=True, null=True)
    decoration_style = models.CharField(verbose_name='装修风格', max_length=30, blank=True, null=True)
    budget = models.FloatField(verbose_name='预算', max_length=10, default=0.0)
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

'''
1 As the Tag Data, we can pick up tag as the data
2 Update the Tag model by detail data.
'''
class Tag(models.Model):
    category = models.ForeignKey(Category, to_field='name', related_name='category_tag_set', null=True, blank=True,verbose_name='分类')
    name = models.CharField(max_length=40, unique=True, verbose_name='名称')
    cited_times = models.PositiveIntegerField(default=0, verbose_name='引用次数')
    average_price = models.FloatField(default=0.0,verbose_name='平均价格')
    min_price = models.FloatField(default=0.0, verbose_name='最低价格')
    max_price = models.FloatField(default=0.0, verbose_name='最高价格')
    city = models.ForeignKey(City, to_field='name', related_name='city_tag_set', null=True, blank=True, verbose_name='城市')

    def __str__(self):
        return self.name + str(self.category)


class BuyPlace(models.Model):
    # city = models.ForeignKey(City, to_field='name')
    name = models.CharField(max_length=50, unique=True)
    latitude = models.FloatField(default=0.0)
    longitude = models.FloatField(default=0.0)
    latitudeE6 = models.FloatField(default=0.0)
    longitudeE6 = models.FloatField(default=0.0)
    address = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    # poitype = models.CharField(max_length=20, null=True, blank=True)
    site = models.URLField(verbose_name='web site', null=True, blank=True)

    def __str__(self):
        return self.name


class SpendDetail(models.Model):
    owner = models.ForeignKey(User, to_field='username')
    price = models.FloatField()
    unit = models.ForeignKey(Currency, to_field='name', null=True, blank=True)
    city = models.ForeignKey(City, to_field='name', null=True, blank=True)
    tag = models.ForeignKey(Tag, to_field='name', null=True, blank=True)
    brand = models.ForeignKey(Brand, to_field='name', null=True, blank=True)
    addr = models.ForeignKey(BuyPlace, to_field='name', null=True, blank=True)
    note = models.TextField(null=True, blank=True)
    image1 = models.ImageField(upload_to='detail/%Y-%m-%d/', blank=True, null=True)
    image2 = models.ImageField(upload_to='detail/%Y-%m-%d/', blank=True, null=True)
    image3 = models.ImageField(upload_to='detail/%Y-%m-%d/', blank=True, null=True)
    image4 = models.ImageField(upload_to='detail/%Y-%m-%d/', blank=True, null=True)
    # created = models.DateTimeField(auto_created=True)
    created = models.DateTimeField(default='2016-01-01 00:00:00')
    modified = models.DateTimeField(auto_now=True)
    local_id = models.IntegerField(default=-1)

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


'''
=======================================================================
'''

class BrandDataWithCityTag(models.Model):
    """
    The data model build from detail data.
    """
    city = models.ForeignKey(City, to_field='name')
    tag = models.ForeignKey(Tag, to_field='name')
    brand = models.ForeignKey(Brand, to_field='name')
    brand_cited_times = models.PositiveIntegerField(default=0)

    def __str__(self):
        return '_'.join((self.city.name, self.tag.name, self.brand.name, str(self.brand_cited_times)))


class ShopDataWithCityTag(models.Model):
    city = models.ForeignKey(City, to_field='name')
    tag = models.ForeignKey(Tag, to_field='name')
    brand = models.ForeignKey(Brand, to_field='name')
    shop = models.ForeignKey(BuyPlace, to_field='name')
    shop_cited_times = models.PositiveIntegerField(default=0)

    def __str__(self):
        return '_'.join((self.city.name, self.tag.name, self.brand.name, self.shop.name, str(self.shop_cited_times)))


class Feedback(models.Model):
    owner = models.ForeignKey(User, to_field='username', verbose_name='用户')
    content = models.TextField(verbose_name='反馈')
    created = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

