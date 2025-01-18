from django.shortcuts import render, redirect
from carros.models import Carro, Marca
from carros.forms import Carro_ModelForm
from django.views import View
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class CarrosListView(ListView):
    model = Carro
    template_name = 'index.html'
    context_object_name = 'carros'

    def get_queryset(self):
        queryset = super().get_queryset().order_by('modelo')
        search = self.request.GET.get('busca') 
        search2 = self.request.GET.get('marca') 
        
        if search or search2:
            if search:
                queryset = queryset.filter(modelo__icontains=search)
            else:
                queryset = queryset.filter(marca__marca=search2)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['marcas'] = Marca.objects.all()  # Add this line to include marcas in the context
        return context

@method_decorator(login_required(login_url='/'), name='dispatch')
class CarroCreateView(CreateView):
    model = Carro
    form_class = Carro_ModelForm
    template_name = 'cadastra_carro.html'
    success_url = '/'

@method_decorator(login_required(login_url='/'), name='dispatch')
class CarroDeleteView(View):
    def get(self, request, pk):
        carro = Carro.objects.get(pk=pk)
        carro.delete()
        return redirect('index')


class CarroDetailView(DetailView):
    model = Carro
    template_name = "detalhe_carro.html"

@method_decorator(login_required(login_url='/'), name='dispatch')
class CarroUpdateView(UpdateView):
    model = Carro
    form_class = Carro_ModelForm
    template_name = "altera.html"

    def get_success_url(self):
        return reverse_lazy('detalha', kwargs={'pk': self.object.pk})

@method_decorator(login_required(login_url='/'), name='dispatch')
class ModelDeleteView(DeleteView):
    model = Carro
    template_name = "apaga.html"
    success_url = '/'
