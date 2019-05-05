from django.conf.urls import url
from . import views
from haystack.views import SearchView
app_name = 'books'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^reader/$', views.reader, name='reader'),
    url(r'^search/$', SearchView(), name='search'),
    url(r'^login/$', views.login, name='login'),
    url(r'^checkall/$', views.checkall, name='checkall'),
    url(r'^register/$', views.register, name='register'),
    url(r'^loginout/$', views.loginout, name='loginout'),
    url(r'^userdetail/(\d+)/$', views.userdetail, name='userdetail'),
    url(r'^updateUserInfo/(\d+)/$', views.updateUserInfo, name='updateUserInfo'),
    url(r'^readerbook/(\d+)/$', views.readerbook, name='readerbook'),
    url(r'^userhistory/(\d+)/$', views.userhistory, name='userhistory'),

    url(r'^upload/$', views.upload, name='upload'),
    url(r'^addarticle/$', views.addarticle, name='addarticle'),
    url(r'^sendemail/$', views.sendemail, name='sendemail'),
    url(r'^ajax/$', views.ajax, name='ajax'),
    url(r'^ajaxdata/$', views.ajaxdata, name='ajaxdata'),
    url(r'^ajaxlogin/$', views.ajaxlogin, name='ajaxlogin'),
    url(r'^verify/$', views.verify, name='verify'),
    url(r'^checkuser/$', views.checkuser, name='checkuser'),
    url(r'^echarts/$', views.echarts, name='echarts'),

]
