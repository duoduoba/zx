"""zx URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from jizhang.views import *
from qrcode_model.views import QRView
from jizhang.data_view import *
from jizhang.logic_views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^auth/$', TestView.as_view()),
    # =======================jizhang urls start==========================================

    url(r'^jz/init/$', InitView.as_view(), name='init'),

    url(r'^jz/categories/$', CategoryListView.as_view(), name='category-list'),
    url(r'^jz/categories/(?P<pk>\d+)/$', CategoryDetailView.as_view(), name='category-detail'),
    url(r'^jz/categories/(?P<pk>\d+)/tags/$', CategoryTagView.as_view(), name='category-tags'),
    #
    url(r'^jz/cities/$', CityListView.as_view(), name='city-list'),
    url(r'^jz/cities/(?P<pk>\d+)/$', CityDetailView.as_view(), name='city-detail'),

    url(r'^jz/currencies/$', CurrencyListView.as_view(), name='currency-detail'),
    url(r'^jz/currencies/(?P<pk>\d+)/$', CurrencyDetailView.as_view(), name='currency-detail'),

    url(r'^jz/brands/$', BrandListView.as_view(), name='brand-list'),
    url(r'^jz/brands/(?P<pk>\d+)/$', BrandDetailView.as_view(), name='brand-detail'),
    #
    url(r'^jz/tags/$', TagListView.as_view(), name='tag-list'),
    url(r'^jz/tags/(?P<pk>\d+)/$', TagDetailView.as_view(), name='tag-detail'),

    url(r'^jz/spend-details/$', SpendDetailListView.as_view(), name='spenddetail-list'),
    url(r'^jz/spend-details/(?P<pk>\d+)/$', SpendDetailEditView.as_view(), name='spenddetail-detail'),
    url(r'^jz/spend-overview/$', SpendOverView.as_view(), name='overview-detail'),
    #
    # # url(r'^jz/tagdata/$', TagDataListView.as_view(), name=''),
    url(r'^jz/tags/hot/$', HotTagsListView.as_view(), name='hot-tags-list'),

    # =======================jizhang urls end============================================
    url(r'^qr/(?P<pk>\d+)/$', QRView.as_view(), name='qr-list'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
