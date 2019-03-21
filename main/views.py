from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import foodmania
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate

def homepage(request):
	return render(request=request,
				  template_name="main/home.html"
		)

def log_in(request):
	return render(
		request=request,
		template_name='main/log-in.html'
		)


def sign_up(request):
	if request.method == "POST":
		form = UserCreationForm(request.POST)
		if form.is_valid():
			user=form.save()
			username = form.cleaned_data.get('username')
			login(request, user)
			return redirect("main:homepage")
		else:
			for msg in form.error_messages:
				print(form.error_messages[msg])
			return render(request = request,template_name = "main/sign-up.html", context={"form":form})

	form = UserCreationForm
	return render(
		request=request,
		template_name='main/sign-up.html',
		context={"form": form}
		)
