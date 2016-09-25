from django.contrib import admin
from jizhang.models import *
# Register your models here.

#
# class CityAdmin(admin.ModelAdmin):
#     list_display = ('province', 'name', 'state',)

admin.site.register(City)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(BuyPlace)
admin.site.register(SpendDetail)
admin.site.register(Province)
admin.site.register(DecorationCompany)
admin.site.register(UserProfile)
admin.site.register(Feedback)

admin.site.register(TagDataWithCity)
admin.site.register(TagDataWithoutCity)
admin.site.register(BrandDataWithCityTag)
admin.site.register(BuyPlaceDataWithCity)

