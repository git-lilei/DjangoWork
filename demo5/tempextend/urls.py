from django.conf.urls import url
from . import views

app_name = 'tempextend'

urlpatterns = [
    url(r'^list/$', views.list, name='list'),
    url(r'^login/$', views.login, name='login'),
]