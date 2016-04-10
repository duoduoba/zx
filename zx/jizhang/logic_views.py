__author__ = 'Administrator'
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from jizhang.models import *
from jizhang.serializers import TagSerializer

'''
get data from data base
'''

'''
get hot tag list based on price/cited_times
'''
class HotTagsListView(APIView):
	def get(self, request, format=None):
		data = request.GET
		try:
			price = data['price']
		except:
			print('no price value from client')
			raise Http404

		import string
		price = string.atoi(price)
		print('get price=%d' % price)

		number = data.get('number',None)
		if not number:
			number = 15
		else:
			number = string.atoi(number)

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
'''
class BrandListView(APIView):
	def get(self, request, tag):
		pass