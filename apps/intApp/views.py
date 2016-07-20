from django.shortcuts import render, redirect
from django.contrib  import messages
import datetime



def index(request):
	return render(request, 'intTemp/index.html')