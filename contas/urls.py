from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('registro/', views.registro, name='registro'),
    path('login/', views.login_form, name='login'),
    path('logout/', views.logout_view, name='logout'),

    
] 
