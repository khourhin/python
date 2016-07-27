from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.news_list, name='news_list'),
    url(r'^news/(?P<pk>[0-9]+)/$', views.news_detail, name='news_detail'),
    url(r'^news/create/$', views.create_news, name='create_news'),
    url(r'^news/(?P<pk>[0-9]+)/edit/$', views.news_edit, name='news_edit'),
]
