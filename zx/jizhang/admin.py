from django.contrib import admin
from jizhang.models import *
# Register your models here.

#
# class CityAdmin(admin.ModelAdmin):
#     list_display = ('province', 'name', 'state',)

class DetailAdmin(admin.ModelAdmin):
	list_display = ('owner', 'price', 'unit', 'tag', 'brand', 'buy_place', 'note', 'created', 'modified', 'local_id', 'image1', 'image2', 'image3', 'image4')
admin.site.register(City)
admin.site.register(Tag)
# admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(BuyPlace)
admin.site.register(SpendDetail, DetailAdmin)
admin.site.register(DecorationCompany)
admin.site.register(UserProfile)
admin.site.register(Feedback)

admin.site.register(TagDataWithCity)
admin.site.register(TagDataWithoutCity)
admin.site.register(BrandDataWithCityTag)
admin.site.register(BuyPlaceDataWithCity)
admin.site.register(AppVersionView)
