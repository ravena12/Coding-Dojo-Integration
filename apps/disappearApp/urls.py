from django.conf.urls import url 
from . import views 

urlpatterns = [
	url(r'^$', views.index, name="my_disappear_index"),
	url(r'^(\bninjas\b)$', views.showNinjas, name="my_disappear_showNinja"),
	url(r'(?P<color>\w+)$', views.ninja, name="my_disappear_ninja"),
	
]


