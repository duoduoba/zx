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

        return Response({'result':'ok'}, status=status.HTTP_201_CREATED)

