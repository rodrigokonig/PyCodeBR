from django.shortcuts import render, redirect

from carros.models import Carro, Marca
from carros.forms import CarroForm



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

def cadastra_carro(request):
    if request.method == 'POST':
        novo_carro_form = CarroForm(request.POST, request.FILES)
        if novo_carro_form.is_valid():
            novo_carro_form.save()
            return redirect('index')
        else:
            pass
    else:
        novo_carro_form = CarroForm()
    return render(request, 'cadastra_carro.html', {'novo_carro_form':novo_carro_form})   