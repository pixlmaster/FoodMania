from django.contrib import admin
from django.urls import path, include

from . import views

app_name="main"

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('login/' ,views.log_in, name='signin' ),
    path('signup/' ,views.sign_up, name= 'signup'),
]
