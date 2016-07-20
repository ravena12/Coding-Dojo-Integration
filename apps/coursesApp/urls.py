from django.conf.urls import url 
from . import views 

urlpatterns = [
	url(r'^$', views.index, name = "my_course_index"),
	url(r'^course$', views.course, name="my_course_course"),
	url(r'^destroy/(?P<id>\d+)$', views.destroy, name="my_course_destroy"),
	url(r'^remove/(?P<id>\d+)$', views.remove, name="my_course_remove"),
	url(r'^user_course$', views.usercourse, name="my_user_course"),
		
]