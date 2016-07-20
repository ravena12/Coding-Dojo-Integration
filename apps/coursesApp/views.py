from django.shortcuts import render, redirect
from .models import Courses
from ..dloginApp.models import User
import datetime
from django.db.models import Count
from django.core.urlresolvers import reverse


def index(request):
	context = {
	'courses': Courses.objects.all(), # select * from courses

	}
	return render(request, 'courseTemp/index.html', context)

def course(request):
	Courses.objects.create(name=request.POST['name'], description =request.POST['description'] )
	print Courses._meta.db_table
	print(Courses.objects.all())
	return redirect(reverse("my_course_index"))


def destroy(request, id):
	context = {
		'remove': Courses.objects.get(id=id),
	}
	return render(request, 'courseTemp/results.html', context)

def remove(request, id):
	test =  Courses.objects.get(id=id)
	if request.POST[u'button'] == 'Yes! I want to delete this':
		test.delete()
	elif request.POST[u'button'] == 'No':
		pass 
	return redirect(reverse("my_course_index"))


def usercourse(request):
	if request.method =='POST':
		our_user = User.objects.get(id = request.POST['user'])
		our_course = Courses.objects.get(id = request.POST['course'])
		our_course.user_id.add(our_user)
		our_course.save()
	c = Courses.objects.annotate(num_users= Count('user_id'))
	# for item in c:
	# 	print item.num_users 
	# 	print item.user_id.all()
	context = {
		"users": User.objects.all(),
		"courses": Courses.objects.all(),
		"count": c
		}
	return render(request, "courseTemp/user_courses.html",context)
