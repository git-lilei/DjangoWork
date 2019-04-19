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
]