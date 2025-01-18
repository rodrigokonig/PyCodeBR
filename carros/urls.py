from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    # path('', views.CarrosView.as_view(), name='index'),
    path('', views.CarrosListView.as_view(), name='index'),
    path('cadastra', views.CadastraCarro.as_view(), name='cadastra')
] 
