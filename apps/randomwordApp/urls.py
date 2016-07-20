from django.conf.urls import url 
from . import views 

urlpatterns = [
	url(r'^$', views.index, name = "my_word_index"),
	url(r'^goback$',views.process, name = "my_word_process"),
	url(r'^showResults$', views.showResults, name = "my_word_results")
	
]