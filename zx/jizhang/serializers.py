# coding��utf-8
from jizhang.models import *
from rest_framework import serializers


class UserProfileSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.name')
    # city = serializers.ReadOnlyField(source='city.name')
    class Meta:
        model = UserProfile


class CategorySerializer(serializers.ModelSerializer):
    # parent = serializers.ReadOnlyField(source='parent.name')
    class Meta:
        model = Category
        # fields = '__all__'

    def validate_parent(self, value):
        if value and value.parent :
            print('parent has prent is not permitted')
            # assert False and "the parent level should < 2"
            return None
        return value


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        # fields = ('id', 'name', 'logo', 'website','description', 'cited_times')

'''
class BrandDataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BrandData
        fields = ('id', 'city', 'name', 'cited_times')
'''


class TagSerializer(serializers.ModelSerializer):
    # category = serializers.ReadOnlyField()
    class Meta:
        model = Tag
        fields = ('id', 'name')


class BuyPlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuyPlace


class SpendDetailSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    created = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    modified = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    buy_place_name = serializers.ReadOnlyField(source='buy_place.place_name')
    # buy_place_area = serializers.ReadOnlyField(source='buy_place.place_area')

    class Meta:
        model = SpendDetail
        fields = '__all__'

    def validate_price(self, value):
        if value < 0.0:
            print('wrong     case : price < 0')
            return None
        return value
    # def validate_cate:


class SpendOverViewSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    created = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = SpendDetail
        fields = ('id', 'owner', 'tag', 'price', 'created')


class BrandDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = BrandDataWithCityTag
        # fields = ('id', 'brand',)


class TagDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = TagDataWithCity


class TagDataWithoudCitySerializer(serializers.ModelSerializer):
    class Meta:
        model = TagDataWithoutCity


class BuyPlaceDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuyPlaceDataWithCity
        # filds = ('brand')


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City


class FeedbackSerializer(serializers.ModelSerializer):
    created = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Feedback


class AppVersionSerializer(serializers.ModelSerializer):
    created = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    cover_start_date = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    cover_end_date = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    class Meta:
        model = AppVersion
