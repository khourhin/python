from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^runjobs/$', views.job_form, name='job_form'),
]
