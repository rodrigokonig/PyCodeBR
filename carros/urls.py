from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('cadastra', views.cadastra_carro, name='cadastra')
] 
