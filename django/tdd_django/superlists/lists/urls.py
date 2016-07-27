from django.conf.urls import url
from lists import views

urlpatterns = [
    # Examples:
    #"The convention I'm using is that URLs without a
    # trailing slash are "action" URLs which modify the database."
    url(r'^new$', views.new_list, name='new_list'),    
    url(r'^(\d+)/$', views.view_list, name='view_list'),
    url(r'^(\d+)/add_item$', views.add_item, name='add_item'),
    
    # url(r'^blog/', include('blog.urls')),

#    url(r'^admin/', include(admin.site.urls)),

]
