from django.conf.urls import url
from . import views
from haystack.views import SearchView
app_name = 'books'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^reader/(\d+)/$', views.reader, name='reader'),
    url(r'^search/$', SearchView(), name='search'),
    url(r'^login/$', views.login, name='login'),
    url(r'^checkall/(\d+)/$', views.checkall, name='checkall'),
    url(r'^register/$', views.register, name='register'),
    url(r'^loginout/$', views.loginout, name='loginout'),
    url(r'^userdetail/(\d+)/$', views.userdetail, name='userdetail'),
    url(r'^updateUserInfo/(\d+)/$', views.updateUserInfo, name='updateUserInfo'),
    url(r'^readerbook/(\d+)/$', views.readerbook, name='readerbook'),
]
