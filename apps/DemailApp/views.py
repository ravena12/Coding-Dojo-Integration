from django.shortcuts import render, redirect
from .models import Email
from django.contrib  import messages
import datetime
from django.core.urlresolvers import reverse


def index(request):
	return render(request, 'DemailTemp/index.html')

def email(request):
	if Email.emailManager.validEmail(request.POST['email']):
		Email.emailManager.create(email=request.POST['email'])
		messages.success(request, "The email address you entered (" + request.POST['email'] + ") is a valid email address! Thank you!")
		return redirect (reverse('my_demail_success'))

	else:
		messages.warning(request, 'Invalid Email!')
		return redirect(reverse("my_demail_index"))

def success(request):
	context = {
		'emails': Email.emailManager.all()
	}
	return render(request, 'DemailTemp/results.html', context)



	#when you create a manager it replaces the objects you make  
	#it will inherit the same functions 
#[::-1]

# start value end value and step value
#html emails.0.email