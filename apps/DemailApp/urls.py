from django.conf.urls import url 
from . import views 

urlpatterns = [
	url(r'^$', views.index, name="my_demail_index"),
	url(r'^email$', views.email, name="my_demail_email"),
	url(r'^success$', views.success, name="my_demail_success"),

		
]