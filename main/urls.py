from django.contrib import admin
from django.urls import path, re_path, include

from . import views

app_name="main"
urlpatterns = [
    path('search', views.search, name = 'search'),
    path('', views.homepage, name='homepage'),
    path('signup/' ,views.sign_up, name= 'signup'),
    path('logout/', views.logout_request, name='logout'),
    path('login/', views.login_request, name='login'),
    path('profile/', views.get_user_profile, name = 'profile'),
    path('profile/logout', views.logout_request, name = 'prof-logout'),
    path('about', views.about, name='about'),
     path('complaint', views.complain, name='complaint'),
    re_path('profile/profile', views.get_user_profile, name = 'prof-prof'),
    re_path('profile/signup', views.sign_up, name = 'prof-signup'),
    path("<single_slug>", views.single_slug, name="single_slug"),
]
