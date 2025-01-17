from django.shortcuts import render

from carros.models import Carro, Marca


def index(request):
    filtro_marca = request.GET.get('marca')  
    filtro_modelo = request.GET.get('busca')
    
    if filtro_marca:
        carros = Carro.objects.filter(marca__marca=filtro_marca)
    elif filtro_modelo:
        carros = Carro.objects.filter(modelo__icontains=filtro_modelo)
    else:
        carros = Carro.objects.all().order_by('modelo')  

    marcas = Marca.objects.all()  
    return render(request, 'index.html', {'carros': carros, 'marcas': marcas})  

