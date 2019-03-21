from django.shortcuts import render
from django.http import HttpResponse
from .models import foodmania

def homepage(request):
	return render(request=request,
				  template_name="main/home.html"
		)

def login(request):
	return render(
		request=request,
		template_name='main/log-in.html'
		)


def signup(request):
	return render(
		request=request,
		template_name='main/sign-up.html',
		context={"details": foodmania.objects.all}
		)
