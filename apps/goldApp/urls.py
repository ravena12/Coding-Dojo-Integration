from django.conf.urls import url 
from . import views 

urlpatterns = [
	url(r'^$', views.index, name = "my_gold_index"),
	url(r'^process_money$', views.process_money, name ="my_gold_process"),
	url(r'^clear$', views.clear, name ="my_gold_clear"),
		
]