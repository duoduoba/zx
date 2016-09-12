# coding=utf8
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
from rest_framework.authtoken import views as authtoken_views


urlpatterns = [
    # url(r'^/', RootView),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-token-auth/',  authtoken_views.obtain_auth_token),
    #for username&password
    url(r'^auth/', Login.as_view()),
    url(r'^register/', RegisterView.as_view()),
    #for mobile register
    #url(r'^login2/', Login2.as_view()),
    url(r'^register2/', RegisterView2.as_view()),
    # =======================jizhang urls start==========================================

    url(r'^jz/init/$', InitView.as_view(), name='init'),
    url(r'^jz/user-profiles/$', UserProfileListView.as_view(), name='profile-list'),
    url(r'^jz/user-profiles/(?P<pk>\d+)/$', UserProfileDetailView.as_view(), name='profile-detail'),

    url(r'^jz/categories/$', CategoryListView.as_view(), name='category-list'),
    url(r'^jz/categories/(?P<pk>\d+)/$', CategoryDetailView.as_view(), name='category-detail'),
    url(r'^jz/categories/(?P<pk>\d+)/tags/$', CategoryTagView.as_view(), name='category-tags'),
    # #
    # url(r'^jz/provinces/$', ProvinceListView.as_view(), name='province-list'),
    url(r'^jz/cities/$', CityListView.as_view(), name='city-list'),
    # url(r'^jz/cities/(?P<pk>\d+)/$', CityDetailView.as_view(), name='city-detail'),

    url(r'^jz/currencies/$', CurrencyListView.as_view(), name='currency-detail'),
    url(r'^jz/currencies/(?P<pk>\d+)/$', CurrencyDetailView.as_view(), name='currency-detail'),

    url(r'^jz/brands/$', BrandListView.as_view(), name='brand-list'),
    url(r'^jz/brands/(?P<pk>\d+)/$', BrandDetailView.as_view(), name='brand-detail'),
    #
    url(r'^jz/tags/$', TagListView.as_view(), name='tag-list'),
    url(r'^jz/tags/(?P<pk>\d+)/$', TagDetailView.as_view(), name='tag-detail'),

    url(r'^jz/buy-places/$', BuyPlaceListView.as_view(), name='buy-place-list'),
    url(r'^jz/buy-places/(?P<pk>\d+)/$', BuyPlaceDetailView.as_view(), name='buy-place-detail'),

    url(r'^jz/details/$', SpendDetailListView.as_view(), name='detail-list'),
    url(r'^jz/details/(?P<pk>\d+)/$', SpendDetailEditView.as_view(), name='detail-detail'),
    # url(r'^jz/spend-overview/$', SpendOverView.as_view(), name='overview-detail'),
    #
    # data recommendation : tag, brand, shop
    url(r'^jz/tags/hot/$', HotTagsListView.as_view(), name='hot-tags-list'),
    url(r'^jz/brands/hot/$', HotBrandListView.as_view(), name='hot-brands-list'),
    url(r'^jz/shops/hot/$', HotShopListView.as_view(), name='hot-brands-list'),

    url(r'^jz/feedback/$', FeedbackView.as_view(), name='feadback-list'),

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
