from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.CarrosListView.as_view(), name='index'),
    path('cadastra', views.CarroCreateView.as_view(), name='cadastra'),
    path('carro/<int:pk>/', views.CarroDetailView.as_view(), name='detalha'),
    path('carro/<int:pk>/atualiza/', views.CarroUpdateView.as_view(), name='altera'),
    path('carro/<int:pk>/apaga/', views.CarroDeleteView.as_view(), name='apaga'),
]
