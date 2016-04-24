#coding: utf-8
# __author__ = 'Administrator'
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from jizhang.models import *
from jizhang.serializers import TagSerializer, BrandDataSerializer, ShopDataSerializer

'''
get data from data base
'''

'''
get hot tag list based on price/cited_times
'''
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

	def get(self, request, format=None):
		data = request.GET
		try:
			price = data['price']
		except:
			print('no price value from client')
			raise Http404

		# import string
		price = float(price)
		number = NumberUtil.number(request)
		print('get price=%d number=%d' % (price, number))

		query_list = Tag.objects.filter(average_price__range=(price - 1000, price + 1000)).order_by('-cited_times')
		query_list = query_list[:number]
		serializer = TagSerializer(query_list, many=True, context={'request': request})

		return Response(serializer.data, status=status.HTTP_200_OK)

'''
get tags under one category name
'''
class CategoryTagView(APIView):
	def get(self, request, pk):
		print('category-tag-set pk=%s' % pk)
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
	def get(self, request):
		data = request.GET
		# print(data)
		sql = {}
		sql['tag'] = data.get('tag', None)
		if data.get('city', None):
			sql['city'] = data.get('city')

		number = NumberUtil.number(request)
		# query_list = BrandDataWithCityTag.objects.filter(tag=tag, city=city).order_by('-brand_cited_times')
		query_list = BrandDataWithCityTag.objects.filter(**sql).order_by('-brand_cited_times')
		query_list = query_list[:number]

		serializer = BrandDataSerializer(query_list, many=True, context={'request': request})
		print('get right data from HoTBrandListView')
		return Response(serializer.data, status=status.HTTP_200_OK)


class HotShopListView(APIView):
	def get(self, request):
		data = request.GET
		sql = {}
		sql['city'] = data.get('city', None)
		'''
		if data.get('city', None):
			sql['city'] = data.get('city')
		else:
			print('not got city data from client')
		if data.get('brand', None):
			sql['brand'] = data.get('brand')
		else:
			print('not got brand data from client')
		# print(sql)
		'''
		number = NumberUtil.number(request)
		query_list = ShopDataWithCityTag.objects.filter(**sql).order_by('-shop_cited_times')
		query_list = query_list[:number]

		serializer = ShopDataSerializer(query_list, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)
