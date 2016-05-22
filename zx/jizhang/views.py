# coding=utf8
import datetime

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework import generics, permissions
from rest_framework.authtoken.views import ObtainAuthToken

from jizhang.serializers import *
from jizhang.permissions import IsOwnerOrReadOnly
from jizhang.log.logger import logger


# Create your views here.


class LoginAndObtainExpiringAuthToken(ObtainAuthToken):
    '''
    Login and get token
    '''

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        now = datetime.datetime.now()
        if not created and token.created < now - datetime.timedelta(seconds=60):
            token.delete()
            token = Token.objects.create(user=user)
            token.created = datetime.datetime.now()
            token.save()
        return Response({'token': token.key})


class RegisterView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, format=None):
        print("debug message")
        logger.info("info message")
        logger.warn("warn message")
        logger.error("error message")
        logger.critical("critical message")
        from django.core.mail import send_mail
        send_mail('test email tile', 'i am email mmkkkkkkkkkkkkkkkkkk', '1211057058@qq.com', ('1211057058@qq.com',))

        return Response('OK')

    def post(self, request, format=None):
        try:
            data = request.data
            username = data['username']
            password = data['password']
            print(username)
            print(password)
        except Exception as ex:
            print('get user name or password data error')
            # raise Http404
            return Response('No username or password data', status=status.HTTP_400_BAD_REQUEST)

        try:
            print('create user....')
            user = User.objects.create(username=username, password=password)
        except Exception as ex:
            return Response('Invalid username', status=status.HTTP_400_BAD_REQUEST)
        # print(user)
        token, created = Token.objects.get_or_create(user=user)
        # token = Token.objects.get_or_create(user=user)
        print(token)
        # result = {'result': 'ok', 'message': token.key}
        return Response({'token': token.key})


class RegisterView_Andorid(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request):
        user = User.objects.get(username='18625177794_')
        return Response('RegisterView_Andorid')

    def random_str(self, randomlength=8):
        str = ''
        chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
        length = len(chars) - 1
        import random
        for i in range(randomlength):
            str += chars[random.randint(0, length)]
        return str

    def post(self, request, format=None):
        try:
            print('enter register from mobile client')
            data = request.data
            username = data['username']
            type = data['type']
            username = username + '_' + type
            user = User.objects.get(username=username)
            if not user:
                password = self.random_str(6)
                print(username)
                print(password)
                user = User.objects.create(username=username, password=password)
            print('------------------')
            print(user.username)
            token, created = Token.objects.get_or_create(user=user)
            print(token)
        except Exception as ex:
            return Response('Invalid username', status=status.HTTP_400_BAD_REQUEST)
        return Response({'token': token.key})


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
            logger.info(province)
            self.queryset = City.objects.filter(province=province)
            logger.info(self.queryset)
        finally:
            # logger.info('22222')
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
    permission_classes = (permissions.IsAuthenticated,)


class TagDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()

    def perform_update(self, serializer):
        if self.request.user.is_superuser:
            super(TagDetailView, self).perform_update(serializer)
        else:
            logger.info('tag can not be modified')
            pass

    def perform_destroy(self, instance):
        if self.request.user.is_superuser:
            super(TagDetailView, self).perform_update(instance)
        else:
            logger.info('tag can not be deleted')
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
            logger.info('submit detail data ,user is -->', request.user.username)
            user = User.objects.get(username=request.user.username)
            logger.info(user)
            userprofile = UserProfile.objects.get(user=user)
            logger.info(userprofile)
            city = userprofile.city
            logger.info(city)
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
