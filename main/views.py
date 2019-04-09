from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Restaurant, Food, complaint, create, Order, Order_content, create_Order, create_Order_cont
from .forms import SignUpForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
import random


def single_slug(request, single_slug):
    Restaurants = [r.Restaurant_slug for r in Restaurant.objects.all()]
    Restaurant_name=single_slug

    matching_Food = Food.objects.filter(Restaurant_items__Restaurant_slug=single_slug)
    return render(request=request,
                 template_name='main/Restaurant.html',
                 context={"matching_Food": matching_Food, "rest_name":Restaurant_name})

def homepage(request):
	return render(request=request,
				  template_name="main/home.html",
				  context={"restaurants":Restaurant.objects.all }
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


#Restaruant Search

def search(request) : 
	if request.method == 'POST' : 
		restaurant_name = request.POST.get('search')
		try :
			status = Restaurant.objects.filter(Restaurant_Name__icontains = restaurant_name)
		except Restaurant.DoesNotExist : 
			status = None
		if status : 
			return render(request, "main/search.html", {"restaurants" : status} )
		else : 
			messages.info(request, f"Your query didn't match any results. Try with another keywords.")
			return redirect('/')
	else : 
		return render(request, "main/search.html", {})
		
		
#display User Profile

def get_user_profile(request) : 
	return render(request, 
					template_name = 'main/user_profile.html'
					)

def about(request):
	return render(request,
					template_name='main/about.html')
					
#end 

def complain(request):
	if request.method == 'POST':
		name= str(request.POST.get('username'))
		usermessage= request.POST.get('Message')
		c=create(name,usermessage)
		c.save()
		messages.info(request, f"Your complaint/query was submitted")
		return redirect("/about")

#checkout 
def cart(request):
	if request.method == 'POST' : 
		messages.info(request, f"Opened Cart")
		name = request.POST.getlist('food_name') 
		price = request.POST.getlist('foodprice') 
		quantity = request.POST.getlist('quantity') 
		Rest_name=request.POST.get('Rest_name')
		
		data = []
		total = 0
		for i in range(len(name))  :
			if quantity[i] is not '' : 
				data.append({'name' : name[i], 'price' : int(price[i]), 'quantity' : int(quantity[i]) } )
				total = total + int(price[i]) * int(quantity[i])
				
		#if not data : 
		#	messages.info(request, f"Atleast one food item should have positive quantity")
		#	return HttpResponseRedirect("")
		
		context = {'data' : data, 'total' : total, 'rest_name':Rest_name}
		return render(request, "main/cart.html" ,
			context )

def checkout(request):
	if request.method == 'POST' : 
		messages.info(request, f"Your Order has been submitted")
		name = request.POST.getlist('food_name') 
		price = request.POST.getlist('foodprice') 
		quantity = request.POST.getlist('quantity') 
		Rest_name=request.POST.get('Rest_name')
		random_int=random.randint(10000,99999)
		total=0
		for i in range(len(name))  :
			if quantity[i] is not '' : 
				total = total + int(price[i]) * int(quantity[i])
		order=create_Order(random_int,total)
		order.save()
		for i in range(len(name))  :
			if quantity[i] is not '' :
				#data.append({'name' : name[i], 'price' : int(price[i]), 'quantity' : int(quantity[i]) } ) 
				content=create_Order_cont(name[i],int(quantity[i]), order)
				content.save()
	return HttpResponse('Checked Out')