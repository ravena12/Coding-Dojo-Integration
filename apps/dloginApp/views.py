from django.shortcuts import render, redirect
from .models import User
from django.contrib  import messages
import datetime
from django.core.urlresolvers import reverse

def index(request):
	return render(request, 'dloginTemp/index.html')

def register(request):
	if User.userManager.isValidReg(request.POST,request):
		passflag = True
		return redirect (reverse("my_login_index"))

	else:
		passflag = False
		return redirect(reverse("my_login_index"))
def login(request):
	if User.userManager.login(request.POST, request):
		context = {
		"user": User.objects.get(email =request.POST['email'])
		}
		passflag=True
		return render(request, 'dloginTemp/results.html', context)
	else: 
		passflag = False

		return redirect(reverse("my_login_index"))


def success(request):
	context = {
		'emails': User.userManager.all()[::-1]
	}
	return render(request, 'dloginTemp/results.html', context)




  
 