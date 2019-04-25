from django.conf.urls import url
from . import views

app_name='branches'

urlpatterns = [
    # /branches/
    url(r'^$',views.index,name='index'),

	# /branches/66
	url(r'^(?P<departments_id>[0-9]+)/$', views.detail, name='detail' ),

   # /branches/66/favorite
   url(r'^(?P<departments_id>[0-9]+)/favorite/$', views.favorite, name='favorite' ),
 ]
