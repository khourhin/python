from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^create/$', views.post_create),
    url(r'^(?P<pk>\d+)/$', views.post_detail, name='detail'),
    url(r'^list/$', views.post_list, name='list'),
    url(r'^(?P<pk>\d+)/edit/$', views.post_update, name='update'),
    url(r'^(?P<pk>\d+)/delete/$', views.post_delete, name='delete'),
]
