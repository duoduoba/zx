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
from jizhang.webview.webviews import *
from django.contrib.auth.views import login, logout
from jizhang.webview.webviews import register, login_after, test



urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^auth/$', LoginAndObtainExpiringAuthToken.as_view()),
    url(r'^api-token-auth/', LoginAndObtainExpiringAuthToken.as_view()),
    url(r'^login/', LoginAndObtainExpiringAuthToken.as_view()),
    url(r'^register/', RegisterView.as_view()),
    url(r'^register2/', RegisterView2.as_view()),
    # =======================jizhang urls start==========================================

    url(r'^jz/init/$', InitView.as_view(), name='init'),

    url(r'^jz/categories/$', CategoryListView.as_view(), name='category-list'),
    url(r'^jz/categories/(?P<pk>\d+)/$', CategoryDetailView.as_view(), name='category-detail'),
    url(r'^jz/categories/(?P<pk>\d+)/tags/$', CategoryTagView.as_view(), name='category-tags'),
    #
    url(r'^jz/provinces/$', ProvinceListView.as_view(), name='province-list'),
    url(r'^jz/cities/$', CityListView.as_view(), name='city-list'),
    url(r'^jz/cities/(?P<pk>\d+)/$', CityDetailView.as_view(), name='city-detail'),

    url(r'^jz/currencies/$', CurrencyListView.as_view(), name='currency-detail'),
    url(r'^jz/currencies/(?P<pk>\d+)/$', CurrencyDetailView.as_view(), name='currency-detail'),

    url(r'^jz/brands/$', BrandListView.as_view(), name='brand-list'),
    url(r'^jz/brands/(?P<pk>\d+)/$', BrandDetailView.as_view(), name='brand-detail'),
    #
    url(r'^jz/tags/$', TagListView.as_view(), name='tag-list'),
    url(r'^jz/tags/(?P<pk>\d+)/$', TagDetailView.as_view(), name='tag-detail'),

    url(r'^jz/shops/$', ShopListView.as_view(), name='shop-list'),
    url(r'^jz/shops/(?P<pk>\d+)/$', ShopDetailView.as_view(), name='shop-detail'),

    url(r'^jz/details/$', SpendDetailListView.as_view(), name='detail-list'),
    url(r'^jz/details/(?P<pk>\d+)/$', SpendDetailEditView.as_view(), name='detail-detail'),
    # url(r'^jz/spend-overview/$', SpendOverView.as_view(), name='overview-detail'),
    #
    # data recommendation : tag, brand, shop
    url(r'^jz/tags/hot/$', HotTagsListView.as_view(), name='hot-tags-list'),
    url(r'^jz/brands/hot/$', HotBrandListView.as_view(), name='hot-brands-list'),
    url(r'^jz/shops/hot/$', HotShopListView.as_view(), name='hot-brands-list'),

    # =======================jizhang urls end============================================
    url(r'^qr/(?P<pk>\d+)/$', QRView.as_view(), name='qr-list'),

    # =========================Web View================================
    url(r'^web/tags/$', get_tags, name='tags'),
    url(r'^web/accounts/LoginView/$', login),
    url(r'^web/accounts/LoginView/index.html/$', login_after),
    url(r'^web/accounts/logout/$', logout),
    url(r'^web/accounts/register/$', register),
    url(r'^web/$', test),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
