from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_delete
from django.dispatch import receiver

class City(models.Model):
    name = models.CharField(max_length=30, unique=True)
    objects = models.Manager()

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    user = models.OneToOneField(User, to_field='username')
    nick_name = models.CharField(max_length=30, null=True, blank=True)
    city = models.ForeignKey(City, to_field='name', related_name='city_user_set')
    picture = models.ImageField(upload_to='user/', blank=True, null=True)
    signature = models.CharField(max_length=30, )

    def __str__(self):
        return '_'.join((self.user.username, self.city.name))

class Category(models.Model):
    name = models.CharField(max_length=20, unique=True)
    parent = models.ForeignKey('self', to_field='name', null=True, blank=True)
    description = models.CharField(max_length=60, null=True, blank=True)

    def __str__(self):
        return self.name


class Currency(models.Model):
    name = models.CharField(max_length=14, unique=True, default='RMB')

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=40, unique=True)
    logo = models.ImageField(upload_to='logo/', null=True, blank=True)
    website_site = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=100, null=True, blank=True)
    cited_times = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

'''
1 As the Tag Data, we can pick up tag as the data
2 Update the Tag model by detail data.
'''
class Tag(models.Model):
    category = models.ForeignKey(Category, to_field='name', related_name='category_tag_set', null=True, blank=True)
    name = models.CharField(max_length=40, unique=True)
    cited_times = models.PositiveIntegerField(default=0)
    average_price = models.FloatField(default=0.0)
    min_price = models.FloatField(default=0.0)
    max_price = models.FloatField(default=0.0)
    city = models.ForeignKey(City, to_field='name', related_name='city_tag_set', null=True, blank=True)

    def __str__(self):
        return self.name + self.category


class Shop(models.Model):
    city = models.ForeignKey(City, to_field='name')
    name = models.CharField(max_length=50, unique=True)
    introduction = models.CharField(max_length=200, null=True, blank=True)
    site = models.URLField(verbose_name='web site', null=True, blank=True)

    def __str__(self):
        return self.name + '_' + self.city


class SpendDetail(models.Model):
    owner = models.ForeignKey(User, to_field='username')
    price = models.FloatField()
    unit = models.ForeignKey(Currency, to_field='name', null=True, blank=True)
    city = models.ForeignKey(City, to_field='name', null=True, blank=True)
    tag = models.ForeignKey(Tag, to_field='name', null=True, blank=True)
    brand = models.ForeignKey(Brand, to_field='name', null=True, blank=True)
    addr = models.ForeignKey(Shop, to_field='name', null=True, blank=True)
    note = models.TextField(null=True, blank=True)
    image1 = models.ImageField(upload_to='detail/', blank=True, null=True)
    image2 = models.ImageField(upload_to='detail/', blank=True, null=True)
    image3 = models.ImageField(upload_to='detail/', blank=True, null=True)
    image4 = models.ImageField(upload_to='detail/', blank=True, null=True)
    created = models.DateTimeField(default='2016-01-01 00:00:00')
    modified = models.DateTimeField(auto_now_add=True)
    local_id = models.IntegerField(default=-1)

    # def __str__(self):
    #     if not self.price:
    #         return "price is empty"
    #     return str(self.price) + '_' + self.tag + '_' + self.brand


@receiver(post_delete, sender=SpendDetail)
def photo_post_delete_handler(sender, **kwargs):
    photo = kwargs['instance']
    print(photo)
    storage, path = photo.original_image.storage, photo.original_image.path
    storage.delete(path)

'''
The data model build from detail data.
'''
class BrandDataWithCityTag(models.Model):
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
    shop = models.ForeignKey(Shop, to_field='name')
    shop_cited_times = models.PositiveIntegerField(default=0)

    def __str__(self):
        return '_'.join((self.city.name, self.tag.name, self.brand.name, self.shop.name, str(self.shop_cited_times)))
