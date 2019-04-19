from django.conf.urls import url
from . import views

app_name = 'booktest'

urlpatterns = [
    url(r'^$', views.index, name='booktest'),
    url(r'^list/$', views.list, name='list'),
    url(r'^detail/(\d+)/$', views.detail, name='detail'),
    url(r'^addbook/$', views.addbook, name='addbook'),
    url(r'^addbookhandler/$', views.addbookhandler, name='addbookhandler'),
    url(r'^addhero/(\d+)/$', views.addhero, name='addhero'),
    url(r'^addherohandler/$', views.addherohandler, name='addherohandler'),
    url(r'^delete/(\d+)/$', views.delete, name='delete'),
    url(r'^deletehero/(\d+)/$', views.deletehero, name='deletehero'),
    url(r'^updatebook/(\d+)/$', views.updatebook, name='updatebook'),
    url(r'^updatebookhandler/(\d+)/$', views.updatebookhandler, name='updatebookhandler'),
    url(r'^updatehero/(\d+)/$', views.updatehero, name='updatehero'),
    url(r'^updateherohandler/(\d+)/$', views.updateherohandler, name='updateherohandler'),
]
