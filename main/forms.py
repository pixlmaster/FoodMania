from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm) : 
	first_name = forms.CharField(max_length = 30)
	last_name = forms.CharField(max_length = 30)
	email = forms.EmailField(max_length = 300)
	profile_url = "";

	class Meta : 
		model = User 
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)
