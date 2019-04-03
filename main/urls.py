from django.contrib import admin
from django.urls import path, re_path, include

from . import views

app_name="main"
urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('signup/' ,views.sign_up, name= 'signup'),
    path('logout/', views.logout_request, name='logout'),
    path('login/', views.login_request, name='login'),
    path('profile/', views.get_user_profile, name = 'profile'),
    path('profile/logout', views.logout_request, name = 'prof-logout'),
    re_path('profile/profile', views.get_user_profile, name = 'prof-prof'),
    re_path('profile/signup', views.sign_up, name = 'prof-signup')
]
