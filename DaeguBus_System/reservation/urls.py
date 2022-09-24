from re import template
from django.urls import path 
from . import views 
from django.contrib.auth import views as auth_views

app_name = 'reservation'

urlpatterns = [ 
    path('' , views.index),
    path('login/', auth_views.LoginView.as_view(
         template_name='reservation/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('join/', views.CreatUser, name='CreatUser'),
]