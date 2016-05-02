from django.contrib import admin
from jizhang.models import *
# Register your models here.


class CityAdmin(admin.ModelAdmin):
	list_display = ('province', 'name', 'state',)

admin.site.register(City, CityAdmin)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Shop)
admin.site.register(SpendDetail)
admin.site.register(Province)
admin.site.register(DecorationCompany)
admin.site.register(UserProfile)