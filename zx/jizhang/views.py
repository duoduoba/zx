# coding=utf8
import datetime
import time
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework import generics, permissions
from rest_framework.authtoken.views import ObtainAuthToken

from jizhang.serializers import *
from jizhang.permissions import IsOwnerOrReadOnly
from jizhang.log.logger import logger
from django.http import HttpResponse, JsonResponse
# from django.contrib.auth import authenticate

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
                logger.info('old user login again')
            except:
                logger.debug('new user enter')
                password = self.random_str(6)
                user = User.objects.create(username=username, password=password)
                logger.info('password=%s' % password)
            # if user not exist, create token

            logger.info('username=%s' % username)
            token, created = Token.objects.get_or_create(user=user)
            logger.info(token)
            try:
                pro = UserProfile.objects.get(user=user)
                logger.info('old profile exist, delete')
                if pro:
                    pro.delete()
            except:
                pass
        except Exception as ex:
            return Response('Invalid username', status=status.HTTP_400_BAD_REQUEST)
        return Response({'token': token.key, 'username': username, })


class UserProfileListView(generics.ListCreateAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )

    def get_queryset(self):
        logger.debug(self.request.user)
        self.queryset = UserProfile.objects.filter(user=self.request.user.username)
        return super(UserProfileListView, self).get_queryset()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def create(self, request, *args, **kwargs):
        logger.info('create user profile data')
        data = request.data
        logger.info(data)
        if data.get('city', None):
            City.objects.get_or_create(name=data.get('city'))
        return super(UserProfileListView, self).create(request, *args, **kwargs)


class UserProfileDetailView(generics.RetrieveUpdateAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

    def get_queryset(self):
        self.queryset = UserProfile.objects.filter(user=self.request.user)
        return super(UserProfileDetailView, self).get_queryset()

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

    def update(self, request, *args, **kwargs):
        data = request.data
        if data.get('city', None):
            City.objects.get_or_create(name=data.get('city'))
        return super(UserProfileDetailView, self).update(request, *args, **kwargs)


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


class BuyPlaceListView(generics.ListCreateAPIView):
    serializer_class = BuyPlaceSerializer
    queryset = BuyPlace.objects.all()
    # permission_classes = (permissions.IsAdminUser,)


class BuyPlaceDetailView(generics.RetrieveUpdateAPIView):
    serializer_class = BuyPlaceSerializer
    queryset = BuyPlace.objects.all()
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

        # buy place data
        place_name = data.get('place_name', None)
        place_area = data.get('place_area', None)
        uid = data.get('uid')
        if place_area is '':
            place_area = None

        logger.info(place_area)
        logger.info(place_name)


        if place_name:
            if not uid:
                uid = place_name
            fields = {}
            fields.update({'place_area': place_area,
                           'place_name': place_name,
                           'latitude': data.get('latitude', 0.0),
                           'longitude': data.get('longitude', 0.0),
                           'latitudeE6': data.get('latitudeE6', 0.0),
                           'longitudeE6': data.get('longitudeE6', 0.0),
                           'address': data.get('address', ''),
                           'phone': data.get('phone', ''),
                           'site': data.get('site', ''),
                           'uid': uid})

            logger.info(fields)
            if place_name:
                obj = None
                try:
                    obj = BuyPlace.objects.get(uid=uid)
                except:
                    pass

                if not obj:
                    logger.info('create new buy-place data')
                    obj = BuyPlace.objects.create(**fields)
                else:
                    logger.info('update buy-place data')
                    obj.latitude = fields['latitude']
                    obj.longitude = fields['longitude']
                    obj.latitudeE6 = fields['latitudeE6']
                    obj.longitudeE6 = fields['longitudeE6']
                    obj.address = fields['address']
                    obj.phone = fields['phone']
                    obj.site = fields['site']
                    obj.save()

                self.place_obj = obj
        else:
            logger.info('user did not submit buy place infor.')


class SpendDetailListView(generics.ListCreateAPIView, GetOrCreateMixin):
    serializer_class = SpendDetailSerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    place_obj = None

    def create(self, request, *args, **kwargs):
        self.start = time.time()
        print('create start..................')
        self.pre_get_or_create(request)
        local_id = request.data.get('local_id')
        user = request.user
        spend_detail_set = user.spend_detail_set
        local_id_db = spend_detail_set.filter(local_id=local_id)
        if local_id_db:
            print('delete old local_id %s' % local_id)
            local_id_db.delete()
        return super(SpendDetailListView, self).create(request, *args, **kwargs)

    def perform_create(self, serializer):
        if not hasattr(self, 'place_obj'):
            serializer.save(owner=self.request.user)
        else:
            serializer.save(owner=self.request.user, buy_place=self.place_obj)
        print('perform_create end................. use time= %d' % (time.time() - self.start))

    def get_queryset(self):
        # self.queryset = SpendDetail.objects.filter(owner=self.request.user)
        self.queryset = SpendDetail.objects.all()
        return super(SpendDetailListView, self).get_queryset()


class SpendDetailEditView(generics.RetrieveUpdateDestroyAPIView, GetOrCreateMixin):
    serializer_class = SpendDetailSerializer
    queryset = SpendDetail.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

    def update(self, request, *args, **kwargs):
        self.pre_get_or_create(request)
        return super(SpendDetailEditView, self).update(request, *args, **kwargs)

    def perform_update(self, serializer):
        if not hasattr(self, 'place_obj'):
            logger.info('udpate spend detail')
            serializer.save()
        else:
            logger.info('update the place obj : %s' % self.place_obj)
            serializer.save(buy_place=self.place_obj)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = SpendDetailSerializer(instance=instance)   #return the data to client to verification
        self.perform_destroy(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)


class FeedbackView(generics.ListCreateAPIView):
    serializer_class = FeedbackSerializer

    def get_queryset(self):
        self.queryset = Feedback.objects.filter(owner=self.request.user)
        return super(FeedbackView, self).get_queryset()

    def perform_create(self, serializer):
        logger.info(self.request.data)
        serializer.save(owner=self.request.user)


class AppVersionView(generics.ListCreateAPIView):
    serializer_class = AppVersionSerializer
    queryset = AppVersion.objects.all()
    # permission_classes = (permissions.IsAdminUser,)


def latest_version(request):
    if request.method == 'GET':
        # res = {'version_code': 0.0}
        versions = AppVersion.objects.all().order_by('-created')
        if not versions:
            logger.error('No App uploaded from Admin')
            return JsonResponse({'Error': 'No App file exist'})
        latest = versions[0]
        serializer = AppVersionSerializer(instance=latest)
        res = serializer.data
        # res['version_code'] = latest.version
        url = download_url(request, latest)
        res.update(url)
        return JsonResponse(res)


def download_url(request, latest_item):
    if request.method == 'GET':
        head = 'http://'
        if request.is_secure():
            head = 'https://'
        res = {'download_url': None}
        res['download_url'] = head + request.get_host() + latest_item.download_url.url
        return res