#encoding: GBK
__author__ = 'Administrator'
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from jizhang.models import *


class InitView(APIView):

	def post(self, request, format=None):
		Category.objects.all().delete()
		Category.objects.create(name=u'设计')
		Category.objects.create(name=u'主材')
		Category.objects.create(name=u'软装')
		Category.objects.create(name=u'家电')
		Category.objects.create(name=u'装修')


		City.objects.all().delete()
		City.objects.create(name=u'南京')
		City.objects.create(name=u'上海')
		City.objects.create(name=u'杭州')
		City.objects.create(name=u'深圳')
		City.objects.create(name=u'北京')

		Currency.objects.all().delete()
		Currency.objects.create(name=u'RMB')

		Brand.objects.all().delete()
		Brand.objects.create(name=u'西门子')
		Brand.objects.create(name=u'海尔')
		Brand.objects.create(name=u'美的')
		Brand.objects.create(name=u'九阳')
		Brand.objects.create(name=u'长虹')
		Brand.objects.create(name=u'格力')
		Brand.objects.create(name=u'三星')
		Brand.objects.create(name=u'博世')

		city = City.objects.get(name='南京')
		Shop.objects.create(city=city, name='金盛国际家具')
		Shop.objects.create(city=city, name='卡子门')
		Shop.objects.create(city=city, name='红太阳装饰城')
		Shop.objects.create(city=city, name='苏宁易购')
		Shop.objects.create(city=city, name='国美')
		Shop.objects.create(city=city, name='苏果超市')
		Shop.objects.create(city=city, name='红星美凯龙卡子门店')
		Shop.objects.create(city=city, name='苏宁乐购仕')
		Shop.objects.create(city=city, name='大洋百货')
		Shop.objects.create(city=city, name='沃尔玛新街口店')
		Shop.objects.create(city=city, name='金鹰江宁店')
		Shop.objects.create(city=city, name='京东商城')


		Tag.objects.all().delete()
		category = Category.objects.get(name=u'家电')
		Tag.objects.create(category=category, name=u'洗衣机', cited_times=2414, average_price=2600,
						   min_price=1200, max_price=4500)
		Tag.objects.create(category=category, name=u'滚筒洗衣机', cited_times=1671, average_price=2700,
						   min_price=1260, max_price=5500)
		Tag.objects.create(category=category, name=u'西门子洗衣机', cited_times=100, average_price=3000, min_price=1999,
						   max_price=6500)
		Tag.objects.create(category=category, name=u'空调', cited_times=2178, average_price=3000,
						   min_price=1200, max_price=5500)
		Tag.objects.create(category=category, name=u'中央空调', cited_times=2840, average_price=25000,
						   min_price=11200, max_price=55500)
		Tag.objects.create(category=category, name=u'32寸液晶电视尺寸', cited_times=255, average_price=1500,
						   min_price=999, max_price=2500)
		Tag.objects.create(category=category, name=u'液晶电视', cited_times=1471, average_price=3050,
						   min_price=899, max_price=19500)
		Tag.objects.create(category=category, name=u'42寸液晶电视尺寸', cited_times=339, average_price=4000,
						   min_price=2500, max_price=9000)
		Tag.objects.create(category=category, name=u'对开门冰箱', cited_times=640, average_price=5500,
						   min_price=3300, max_price=8000)
		Tag.objects.create(category=category, name=u'豆浆机', cited_times=1430, average_price=400,
						   min_price=155, max_price=600)
		Tag.objects.create(category=category, name=u'电饭煲', cited_times=1507, average_price=200,
						   min_price=80, max_price=360)

		BrandDataWithCityTag.objects.all().delete()
		ShopDataWithCityTag.objects.all().delete()

		tag = Tag.objects.get(name=u'洗衣机')
		brand = Brand.objects.get(name=u'博世')
		cited_time = 2334
		BrandDataWithCityTag.objects.create(city=city, tag=tag, brand=brand, brand_cited_times=cited_time)
		shop = Shop.objects.get(name=u'红太阳装饰城')
		ShopDataWithCityTag.objects.create(tag=tag, city=city, brand=brand, shop=shop, shop_cited_times=2322)

		tag = Tag.objects.get(name=u'洗衣机')
		brand = Brand.objects.get(name=u'西门子')
		cited_time = 2554
		BrandDataWithCityTag.objects.create(city=city, tag=tag, brand=brand, brand_cited_times=cited_time)
		shop = Shop.objects.get(name=u'苏宁易购')
		ShopDataWithCityTag.objects.create(tag=tag, city=city, brand=brand, shop=shop, shop_cited_times=4333)

		tag = Tag.objects.get(name=u'洗衣机')
		brand = Brand.objects.get(name=u'三星')
		cited_time = 2500
		BrandDataWithCityTag.objects.create(city=city, tag=tag, brand=brand, brand_cited_times=cited_time)
		shop = Shop.objects.get(name=u'金鹰江宁店')
		ShopDataWithCityTag.objects.create(tag=tag, city=city, brand=brand, shop=shop, shop_cited_times=1985)

		tag = Tag.objects.get(name=u'洗衣机')
		brand = Brand.objects.get(name=u'海尔')
		cited_time = 1233
		BrandDataWithCityTag.objects.create(city=city, tag=tag, brand=brand, brand_cited_times=cited_time)
		shop = Shop.objects.get(name=u'大洋百货')
		ShopDataWithCityTag.objects.create(tag=tag, city=city, brand=brand, shop=shop, shop_cited_times=1985)
		shop = Shop.objects.get(name=u'苏宁乐购仕')
		ShopDataWithCityTag.objects.create(tag=tag, city=city, brand=brand, shop=shop, shop_cited_times=2333)
		shop = Shop.objects.get(name=u'国美')
		ShopDataWithCityTag.objects.create(tag=tag, city=city, brand=brand, shop=shop, shop_cited_times=1224)
		shop = Shop.objects.get(name=u'金鹰江宁店')
		ShopDataWithCityTag.objects.create(tag=tag, city=city, brand=brand, shop=shop, shop_cited_times=2121)
		shop = Shop.objects.get(name=u'金盛国际家具')
		ShopDataWithCityTag.objects.create(tag=tag, city=city, brand=brand, shop=shop, shop_cited_times=2222)
		shop = Shop.objects.get(name=u'京东商城')
		ShopDataWithCityTag.objects.create(tag=tag, city=city, brand=brand, shop=shop, shop_cited_times=1211)
		shop = Shop.objects.get(name=u'红星美凯龙卡子门店')
		ShopDataWithCityTag.objects.create(tag=tag, city=city, brand=brand, shop=shop, shop_cited_times=32)


		tag = Tag.objects.get(name=u'液晶电视')
		brand = Brand.objects.get(name=u'海尔')
		cited_time = 1333
		BrandDataWithCityTag.objects.create(city=city, tag=tag, brand=brand, brand_cited_times=cited_time)
		shop = Shop.objects.get(name=u'苏宁乐购仕')
		ShopDataWithCityTag.objects.create(tag=tag, city=city, brand=brand, shop=shop, shop_cited_times=2542)

		tag = Tag.objects.get(name=u'电饭煲')
		brand = Brand.objects.get(name=u'九阳')
		cited_time = 2551
		BrandDataWithCityTag.objects.create(city=city, tag=tag, brand=brand, brand_cited_times=cited_time)
		shop = Shop.objects.get(name=u'苏宁乐购仕')
		ShopDataWithCityTag.objects.create(tag=tag, city=city, brand=brand, shop=shop, shop_cited_times=4333)

		tag = Tag.objects.get(name=u'滚筒洗衣机')
		brand = Brand.objects.get(name=u'西门子')
		cited_time = 3235
		BrandDataWithCityTag.objects.create(city=city, tag=tag, brand=brand, brand_cited_times=cited_time)
		shop = Shop.objects.get(name=u'苏宁乐购仕')
		ShopDataWithCityTag.objects.create(tag=tag, city=city, brand=brand, shop=shop, shop_cited_times=4333)

		tag = Tag.objects.get(name=u'对开门冰箱')
		brand = Brand.objects.get(name=u'海尔')
		cited_time = 1998
		BrandDataWithCityTag.objects.create(city=city, tag=tag, brand=brand, brand_cited_times=cited_time)
		shop = Shop.objects.get(name=u'苏宁易购')
		ShopDataWithCityTag.objects.create(tag=tag, city=city, brand=brand, shop=shop, shop_cited_times=4333)

		tag = Tag.objects.get(name=u'对开门冰箱')
		brand = Brand.objects.get(name=u'博世')
		cited_time = 1055
		BrandDataWithCityTag.objects.create(city=city, tag=tag, brand=brand, brand_cited_times=cited_time)
		shop = Shop.objects.get(name=u'苏宁乐购仕')
		ShopDataWithCityTag.objects.create(tag=tag, city=city, brand=brand, shop=shop, shop_cited_times=4333)

		tag = Tag.objects.get(name=u'对开门冰箱')
		brand = Brand.objects.get(name=u'西门子')
		cited_time = 3636
		BrandDataWithCityTag.objects.create(city=city, tag=tag, brand=brand, brand_cited_times=cited_time)
		shop = Shop.objects.get(name=u'苏宁乐购仕')
		ShopDataWithCityTag.objects.create(tag=tag, city=city, brand=brand, shop=shop, shop_cited_times=4333)

		tag = Tag.objects.get(name=u'电饭煲')
		brand = Brand.objects.get(name=u'美的')
		cited_time = 1995
		BrandDataWithCityTag.objects.create(city=city, tag=tag, brand=brand, brand_cited_times=cited_time)
		shop = Shop.objects.get(name=u'沃尔玛新街口店')
		ShopDataWithCityTag.objects.create(tag=tag, city=city, brand=brand, shop=shop, shop_cited_times=4333)

		return Response({'result': u'init data ok'}, status=status.HTTP_201_CREATED)

