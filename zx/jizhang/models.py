from django.db import models
from django.contrib.auth.models import User


class City(models.Model):
    name = models.CharField(max_length=30, unique=True)


class UserProfile(models.Model):
    user = models.OneToOneField(User, to_field='username')
    nick_name = models.CharField(max_length=30, unique=True)
    city = models.ForeignKey(City, to_field='name', related_name='city_user_set')
    picture = models.ImageField(upload_to='user/', blank=True, null=True)
    signature = models.CharField(max_length=30, )


class Category(models.Model):
    name = models.CharField(max_length=20, unique=True)
    parent = models.ForeignKey('self', to_field='name', null=True, blank=True)
    description = models.CharField(max_length=60, null=True, blank=True)

    def __unicode__(self):
        return self.name


class Currency(models.Model):
    name = models.CharField(max_length=14, unique=True, default='RMB')

    def __unicode__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=40, unique=True)
    logo = models.ImageField(upload_to='logo/', null=True, blank=True)
    webite_site = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=100, null=True, blank=True)
    cited_times = models.PositiveIntegerField(default=0)

    def __unicode__(self):
        return self.name


class Tag(models.Model):
    category = models.ForeignKey(Category, to_field='name', related_name='category_tag_set', null=True, blank=True)
    name = models.CharField(max_length=40, unique=True)
    cited_times = models.PositiveIntegerField(default=0)
    average_price = models.FloatField(default=0.0)
    min_price = models.FloatField(default=0.0)
    max_price = models.FloatField(default=0.0)

    def __unicode__(self):
        return self.name + self.category


class Shop(models.Model):
    city = models.ForeignKey(City, to_field='name', null=True, blank=True)
    addr = models.CharField(max_length=50)


class SpendDetail(models.Model):
    owner = models.ForeignKey(User, to_field='username')
    price = models.FloatField()
    unit = models.ForeignKey(Currency, to_field='name', null=True, blank=True)
    tag = models.ForeignKey(Tag, to_field='name', null=True, blank=True)
    brand = models.ForeignKey(Brand, to_field='name', null=True, blank=True)
    note = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='detail/', blank=True, null=True)
    created = models.DateTimeField(default='2016-01-01 00:00:00')
    modified = models.DateTimeField(auto_now_add=True)

