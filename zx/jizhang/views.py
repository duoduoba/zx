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
from django.contrib.auth import authenticate


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
        # do not use expiring token anymore
        # return Response({'token': token.key})
        now = datetime.datetime.now()
        if not created and token.created < now - datetime.timedelta(seconds=60):
            token.delete()
            token = Token.objects.create(user=user)
            token.created = datetime.datetime.now()
            token.save()
        return Response({'token': token.key})


class Login(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request, *args, **kwargs):
        try:
            data = request.data
            username = data['username']
            password = data['password']
            logger.debug(username)
            logger.debug(password)
            user = User.objects.get(username=username)
            if user and user.check_password(password):
                token, created = Token.objects.get_or_create(user=user)
                logger.debug(token)
                logger.debug(created)
                return Response({'token': token.key})
            else:
                return Response('User not exist', status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            return Response('Invalid username or password data', status=status.HTTP_400_BAD_REQUEST)


class RegisterView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, format=None):
        # print("debug message")
        logger.debug("debug message")
        logger.info("info message")
        logger.warn("warn message")
        logger.error("error message")
        logger.critical("critical message")
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

'''
class Login2(APIView):
    def post(request, format=None):
        data = request.data
        username = data['username']
        type = data['type']
        username = username + '_' + type
        logger.debug(username)
        try:
            user = User.objects.get(username=username)
        except Exception as ex:
            raise('Invalid username')

        token, created = Token.objects.get_or_create(user=user)
        logger.debug(token)
        return Response({'token': token.key})
'''

class RegisterView2(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request):
        return Response('RegisterView2')

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
            logger.info('enter register from mobile client')
            data = request.data
            username = data['username']
            type = data['type']
            username = username + '_' + type
            logger.debug(username)

            # if user exist , delete token and create new token.
            try:
                logger.debug('check user name')
                user = User.objects.get(username=username)
                if user:
                    logger.debug('delete user')
                    user.delete()
            except Exception as ex:
                pass

            # if user not exist, create token
            logger.debug('new user enter register2')
            password = self.random_str(6)
            logger.info('username=%s' % username)
            logger.info('password=%s' % password)
            user = User.objects.create(username=username, password=password)
            logger.info('create user finish')
            token, created = Token.objects.get_or_create(user=user)
            logger.info(token)

            city = City.objects.get(name='南京')
            UserProfile.objects.get_or_create(user=user, city=city)
        except Exception as ex:
            return Response('Invalid username', status=status.HTTP_400_BAD_REQUEST)
        return Response({'token': token.key, 'username': username, })


class UserProfileListView(generics.ListCreateAPIView):
    serializer_class = UserProfileSerializer

    def get_queryset(self):
        logger.debug(self.request.user)
        self.queryset = UserProfile.objects.filter(user=self.request.user.username)
        return super(UserProfileListView, self).get_queryset()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class UserProfileDetailView(generics.RetrieveUpdateAPIView):
    serializer_class = UserProfileSerializer

    def get_queryset(self):
        self.queryset = UserProfile.objects.filter(user=self.request.user)
        return super(UserProfileDetailView, self).get_queryset()

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)


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
    # permission_classes = (permissions.IsAuthenticated,)


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
    queryset = BuyPlace.objects.all()
    # permission_classes = (permissions.IsAdminUser,)


class ShopDetailView(generics.RetrieveUpdateAPIView):
    serializer_class = ShopSerializer
    queryset = BuyPlace.objects.all()
    # permission_classes = (permissions.IsAdminUser,)


class GetOrCreateMixin():
    def pre_get_or_create(self, request):
        data = request.data
        tag = data.get('tag', None)
        print(data)
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
            BuyPlace.objects.get_or_create(name=addr, city=city)


class SpendDetailListView(generics.ListCreateAPIView, GetOrCreateMixin):
    serializer_class = SpendDetailSerializer

    def create(self, request, *args, **kwargs):
        logger.info('sync the detailed data')
        self.pre_get_or_create(request)
        return super(SpendDetailListView, self).create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        self.queryset = SpendDetail.objects.filter(owner=self.request.user)
        # self.queryset = SpendDetail.objects.all()
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


class FeedbackView(generics.ListCreateAPIView):
    serializer_class = FeedbackSerializer

    def get_queryset(self):
        self.queryset = Feedback.objects.filter(owner=self.request.user)
        return super(FeedbackView, self).get_queryset()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
