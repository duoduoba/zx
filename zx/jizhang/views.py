# coding=utf8
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


class ProvinceListView(generics.ListCreateAPIView):
    serializer_class = ProvinceSerializer
    queryset = Province.objects.all()


class CityListView(generics.ListCreateAPIView):
    serializer_class = CitySerializer

    def get_queryset(self):
        self.queryset = City.objects.all()
        try:
            province = self.request.query_params['province']
            print(province)
            self.queryset = City.objects.filter(province=province)

            print(self.queryset)
        finally:
            print('22222')
            return super(CityListView, self).get_queryset()


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


class GetOrCreateMixin():
    def pre_get_or_create(self, request):
        data = request.data
        tag = data.get('tag', None)
        if tag:
            Tag.objects.get_or_create(name=tag)
        brand = data.get('brand', None)
        if brand:
            Brand.objects.get_or_create(name=brand)
        addr = data.get('addr', None)
        if addr:
            print('submit detail data ,user is -->', request.user.username)
            user = User.objects.get(username=request.user.username)
            print(user)
            userprofile = UserProfile.objects.get(user=user)
            print(userprofile)
            city = userprofile.city
            print(city)
            Shop.objects.get_or_create(name=addr, city=city)


class SpendDetailListView(generics.ListCreateAPIView, GetOrCreateMixin):
    serializer_class = SpendDetailSerializer

    def create(self, request, *args, **kwargs):
        self.pre_get_or_create(request)
        return super(SpendDetailListView, self).create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        self.queryset = SpendDetail.objects.filter(owner=self.request.user)
        self.queryset = SpendDetail.objects.all()
        return super(SpendDetailListView, self).get_queryset()


class SpendDetailEditView(generics.RetrieveUpdateDestroyAPIView, GetOrCreateMixin):
    serializer_class = SpendDetailSerializer
    queryset = SpendDetail.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

    def update(self, request, *args, **kwargs):
        self.pre_get_or_create(request)
        return super(SpendDetailEditView, self).update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = SpendDetailSerializer(instance=instance)
        self.perform_destroy(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)