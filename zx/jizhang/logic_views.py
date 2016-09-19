# coding: utf-8
# __author__ = 'Administrator'
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404, HttpResponse
from rest_framework import generics, permissions
from jizhang.serializers import *
from jizhang.models import *
from jizhang.log.logger import logger


def get_city(detail_item):
	city = None
	if detail_item.owner.user_profile:
		city = detail_item.owner.user_profile.city
	return city


def calculate_tag_data(tag, city, price):
	obj = None
	try:
		if city:
			obj = TagDataWithCity.objects.get(tag=tag, city=city)
		else:
			obj = TagDataWithoutCity.objects.get(tag=tag)
	except:
		pass

	if not obj:
		if city:
			obj = TagDataWithCity.objects.create(tag=tag, city=city, average_price=price, min_price=price, max_price=price)
		else:
			obj = TagDataWithoutCity.objects.create(tag=tag, average_price=price, min_price=price, max_price=price)
	else:
		obj.average_price = (obj.average_price * obj.cited_times + price) / (obj.cited_times + 1)
		obj.cited_times += 1
		if city:
			obj.city = city
		if obj.min_price > price:
			obj.min_price = price
		if obj.max_price < price:
			obj.max_price = price
		obj.save()

def generate_tag_data(request):
	# if not request.user.is_superuser:
	# 	print('not valid user')
	# 	return HttpResponse('not valid user!')
	TagDataWithCity.objects.all().delete()
	TagDataWithoutCity.objects.all().delete()

	details = SpendDetail.objects.all()
	print(details.count())
	for item in details:
		tag = item.tag
		city = get_city(item)
		price = item.price
		if not city or not tag:
			continue

		logger.info('tag={} price={} city={}'.format(tag, price, city))
		calculate_tag_data(tag, city, price)
		calculate_tag_data(tag, None, price)
		# 计算城市分类
		# obj = None
		# try:
		# 	obj = TagDataWithCity.objects.get(tag=tag, city=city)
		# except:
		# 	pass
        #
		# if not obj:
		# 	obj = TagDataWithCity.objects.create(tag=tag, city=city, average_price=price, min_price=price, max_price=price)
		# else:
		# 	obj.average_price = (obj.average_price * obj.cited_times + price) / (obj.cited_times + 1)
		# 	obj.cited_times += 1
		# 	obj.city = city
		# 	if obj.min_price > price:
		# 		obj.min_price = price
		# 	if obj.max_price < price:
		# 		obj.max_price = price
		# obj.save()

	return HttpResponse('create tag data finish...!')


def generate_brand_data(request):
	# if not request.user.is_superuser:
	# 	print('not valid user')
	# 	return HttpResponse('not valid user!')

	BrandDataWithCityTag.objects.all().delete()
	details = SpendDetail.objects.all()
	for item in details:
		tag = item.tag
		brand = item.brand
		city = get_city(item)
		logger.info('tag={} brand={} city={}'.format(tag, brand, city))
		if not tag or not brand or not city:
			continue
		obj, created = BrandDataWithCityTag.objects.get_or_create(tag=tag, brand=brand, city=city)
		logger.info('obj={} created={} '.format(obj, created))
		if not created:
			obj.cited_times += 1
			obj.save()
	logger.info('create brand data end')
	return HttpResponse('create brand data finish...!!')


def generate_buy_place_data(request):
	# if not request.user.is_superuser:
	# 	print('not valid user')
	# 	return HttpResponse('not valid user!')
	BuyPlaceDataWithCity.objects.all().delete()
	details = SpendDetail.objects.all()
	for item in details:
		city = get_city(item)
		buy_place_name = None
		if item.buy_place:
			buy_place_name = item.buy_place.place_name

		if not buy_place_name:
			continue
		logger.info('city={} buy_place_name={}'.format(city, buy_place_name))
		obj, created = BuyPlaceDataWithCity.objects.get_or_create(city=city, buy_place_name=buy_place_name)
		if not created:
			obj.cited_times += 1
			obj.save()
	return HttpResponse('create buy place data finish...!!')


class TagDataListView(generics.ListAPIView):
	serializer_class = TagDataSerializer
	queryset = TagDataWithCity.objects.all()
	# permission_classes = (permissions.IsAuthenticatedOrReadOnly, )


class TagDataWithoutCityListView(generics.ListAPIView):
	serializer_class = TagDataWithoudCitySerializer
	queryset = TagDataWithoutCity.objects.all()
	# permission_classes = (permissions.IsAuthenticatedOrReadOnly, )


class BrandDataListView(generics.ListAPIView):
	serializer_class = BrandDataSerializer
	queryset = BrandDataWithCityTag.objects.all()
	# permission_classes = (permissions.IsAuthenticatedOrReadOnly, )


class BuyPlaceDataListView(generics.ListAPIView):
	serializer_class = BuyPlaceDataSerializer
	queryset = BuyPlaceDataWithCity.objects.all()


class NumberUtil():
	@staticmethod
	def number(request):
		data = request.GET
		number = data.get('number', None)
		if not number:
			number = 30
		else:
			# import string
			number = int(number)
		return number


class HotTagsListView(APIView):
	'''
	根据价格，获取热门标签
	'''
	def get(self, request, format=None):
		data = request.GET
		try:
			price = data['price']
		except:
			logger.info('no price value from client')
			raise Http404

		# import string
		price = float(price)
		number = NumberUtil.number(request)
		logger.info('get price=%d number=%d' % (price, number))

		# query_list = TagDataWithCity.objects.filter(average_price__range=(price - 1000, price + 1000)).order_by('-cited_times')
		query_list = TagDataWithoutCity.objects.filter(average_price__range=(price - 1000, price + 1000)).order_by('-cited_times')
		query_list = query_list[:number]
		serializer = TagDataWithoudCitySerializer(query_list, many=True, context={'request': request})

		return Response(serializer.data, status=status.HTTP_200_OK)


class CategoryTagView(APIView):
	'''
	get tags under one category name
	'''
	def get(self, request, pk):
		logger.info('category-tag-set pk=%s' % pk)
		category_obj = Category.objects.get(pk=pk)
		query_set = category_obj.category_tag_set
		tags = TagSerializer(query_set, many=True, context={'request': request})
		return Response(tags.data, status=status.HTTP_200_OK)

'''
	get brand list with city and tag data
	argument:
	1: tag name
	2: city name
	style:
'''


class HotBrandListView(APIView):
	# permission_classes = (permissions.IsAuthenticatedOrReadOnly, )

	def get(self, request):
		data = request.GET
		# logger.info(data)
		sql = {}
		sql['tag'] = data.get('tag', None)
		try:
			user = User.objects.get(username=request.user.username)
			logger.info(user)
			sql['city'] = UserProfile.objects.get(user=user).city
		except:
			return Response('Invalid User Error!')
		
		number = NumberUtil.number(request)
		query_list = BrandDataWithCityTag.objects.filter(**sql).order_by('-cited_times')
		query_list = query_list[:number]

		serializer = BrandDataSerializer(query_list, many=True, context={'request': request})
		logger.info('get right data from HoTBrandListView')
		return Response(serializer.data, status=status.HTTP_200_OK)


class HotShopListView(APIView):
	def get(self, request):
		sql = {}
		try:
			user = User.objects.get(username=request.user.username)
			sql['city'] = UserProfile.objects.get(user=user).city
			logger.info(sql)
		except:
			return Response('Invalid User Error!')
		number = NumberUtil.number(request)
		query_list = BuyPlaceDataWithCity.objects.filter(**sql).order_by('-cited_times')
		query_list = query_list[:number]

		serializer = BuyPlaceDataSerializer(query_list, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)
