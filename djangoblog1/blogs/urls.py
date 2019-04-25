from django.conf.urls import url
from . import views
from .feed import BlogFeed
app_name = 'blogs'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^blogdetail/(\d+)/$', views.blogdetail, name='blogdetail'),
    url(r'^archives/(\d+)/(\d+)/$', views.archives, name='archives'),
    url(r'^category/(\d+)/$', views.category, name='category'),
    url(r'^tag/(\d+)/$', views.tag, name='tag'),
    url(r'^rss/$', BlogFeed(), name='rss'),
]
