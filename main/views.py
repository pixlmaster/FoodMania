from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Restaurant, Food
from .forms import SignUpForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User


def single_slug(request, single_slug):
    Restaurants = [r.Restaurant_slug for r in Restaurant.objects.all()]

    matching_Food = Food.objects.filter(Restaurant_items__Restaurant_slug=single_slug)
    return render(request=request,
                 template_name='main/Restaurant.html',
                 context={"matching_Food": matching_Food})

def homepage(request):
	return render(request=request,
				  template_name="main/home.html",
				  context={"restaurants":Restaurant.objects.all}
			)

def sign_up(request):
	if request.method == "POST":
		form = SignUpForm(request.POST)
		if form.is_valid():
			user=form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f"New Account Created: {username}")
			messages.info(request, f"you are now logged in as {username}")
			login(request, user)
			return redirect("main:homepage")
		else:
			for msg in form.error_messages:
				messages.error(request,f"{msg}: {form.error_messages[msg]}")
			return render(request = request,template_name = "main/sign-up.html", context={"form":form})

	form = SignUpForm()
	return render(
		request=request,
		template_name='main/sign-up.html',
		context={"form": form}
		)
def logout_request(request):
	logout(request)
	messages.info(request, "Logged out successfully!")
	return redirect("main:homepage") 
def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('/')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request = request,
                    template_name = "main/login.html",
                    context={"form":form} )


#display User Profile

def get_user_profile(request) : 
	return render(request, 
					template_name = 'main/user_profile.html'
					)

def about(request):
	return render(request,
					template_name='main/about.html')
#end 

