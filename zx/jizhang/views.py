from django.shortcuts import render
# from .permissions import IsOwnerOrReadOnly
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
# from django.core.exceptions import ObjectDoesNotExist
from django.contrib import auth
from jizhang.serializers import *
from rest_framework import generics, permissions
from django.http import Http404
from jizhang.permissions import IsOwnerOrReadOnly
from django.views.decorators.csrf import csrf_exempt,csrf_protect
# Create your views here.


class TestView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, format=None):
        print('get test view')
        return Response('OK')

    def post(self, request, format=None):
        try:
            data = request.data
        except Exception as e:
            print('get request.data error')
            return Response(e.message)

        if not ('username' in data and 'password' in data):
            return Response('No username and passwd', status=status.HTTP_401_UNAUTHORIZED)

        username = data['username']
        password = data['password']
        user = auth.authenticate(username=username, password=password)
        if not user:
            return Response('user name or password is wrong!')
        token = Token.objects.get_or_create(user=user)
        return Response({'token': token[0].key})


class CategoryListView(generics.ListCreateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    # permission_classes = (permissions.IsAdminUser,)


class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    # permission_classes = (permissions.IsAdminUser,)


class CityListView(generics.ListCreateAPIView):
    serializer_class = CitySerializer
    queryset = City.objects.all()


class CityDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CitySerializer
    queryset = City.objects.all()


class CurrencyListView(generics.ListCreateAPIView):
    serializer_class = CurrencySerializer
    queryset = Currency.objects.all()


class CurrencyDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CurrencySerializer
    queryset = Currency.objects.all()


class BrandListView(generics.ListCreateAPIView):
    serializer_class = BrandSerializer
    queryset = Brand.objects.all()


class BrandDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BrandSerializer
    queryset = Brand.objects.all()


class TagListView(generics.ListCreateAPIView):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()


class TagDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()

    def perform_update(self, serializer):
        if self.request.user.is_superuser:
            super(TagDetailView, self).perform_update(serializer)
        else:
            print('tag can not be modified')
            pass

    def perform_destroy(self, instance):
        if self.request.user.is_superuser:
            super(TagDetailView, self).perform_update(instance)
        else:
            print('tag can not be deleted')
            pass


class ShopListView(generics.ListCreateAPIView):
    serializer_class = ShopSerializer
    queryset = Shop.objects.all()
    # permission_classes = (permissions.IsAdminUser,)


class ShopDetailView(generics.RetrieveUpdateAPIView):
    serializer_class = ShopSerializer
    queryset = Shop.objects.all()
    # permission_classes = (permissions.IsAdminUser,)


class SpendDetailListView(generics.ListCreateAPIView):
    serializer_class = SpendDetailSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        self.queryset = SpendDetail.objects.filter(owner=self.request.user)
        return super(SpendDetailListView, self).get_queryset()


class SpendDetailEditView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SpendDetailSerializer
    queryset = SpendDetail.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

'''
class SpendOverView(generics.ListAPIView):
    serializer_class = SpendOverViewSerializer
    # queryset = SpendDetail.objects.filter(owner=self.request.user)

    def get_queryset(self):
        self.queryset = SpendDetail.objects.filter(owner=self.request.user)
        return super(SpendOverView, self).get_queryset()
'''