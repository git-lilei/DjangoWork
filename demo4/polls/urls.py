from django.conf.urls import url
from . import views

app_name = 'polls'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^list/$', views.list, name='list'),
    url(r'^detail/(\d+)/$', views.detail, name='detail'),
    url(r'^vote/(\d+)/$', views.vote, name='vote'),
    url(r'^addquestion/$', views.addquestion, name='addquestion'),
    url(r'^addquehandler/$', views.addquehandler, name='addquehandler'),
    url(r'^addchoose/(\d+)/$', views.addchoose, name='addchoose'),
    url(r'^addchoosehandler/$', views.addchoosehandler, name='addchoosehandler'),
    url(r'^deletequestion/(\d+)/$', views.deletequestion, name='deletequestion'),
    url(r'^deletechoose/(\d+)/$', views.deletechoose, name='deletechoose'),
    url(r'^updatequestion/(\d+)/$', views.updatequestion, name='updatequestion'),
    url(r'^updatequehandler/(\d+)/$', views.updatequehandler, name='updatequehandler'),
    url(r'^updatechoose/(\d+)/$', views.updatechoose, name='updatechoose'),
    url(r'^updatechoosehandler/(\d+)/$', views.updatechoosehandler, name='updatechoosehandler'),

]