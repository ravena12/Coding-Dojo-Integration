from django.conf.urls import url 
from . import views 

urlpatterns = [
	url(r'^$', views.index, name="my_login_index"),
	url(r'^register$', views.register, name="my_login_register"),
	url(r'^success/$', views.success, name="my_login_success"),
	url(r'^login$', views.login, name="my_login_login"),
		
]