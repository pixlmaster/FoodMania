from django.contrib import admin
from django.urls import path, re_path, include

from . import views

app_name="main"
urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('signup/' ,views.sign_up, name= 'signup'),
    path('logout/', views.logout_request, name='logout'),
    path('login/', views.login_request, name='login'),
    re_path('profile/(?P<username>[a-zA-Z0-9]+)$', views.get_user_profile, name = 'profile'),
]
