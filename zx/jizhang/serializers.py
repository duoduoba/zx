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
        fields = ('id', 'category', 'name')


class ShopSerializer(serializers.ModelSerializer):
    city = serializers.ReadOnlyField(source='city.name')
    band = serializers.ReadOnlyField(source='brand.name')
    class Meta:
        model = Shop


class SpendDetailSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    created = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    modified = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

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


class ShopDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShopDataWithCityTag
        # filds = ('brand')


class ProvinceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Province


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City


class FeedbackSerializer(serializers.ModelSerializer):
    created = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Feedback
