from django.shortcuts import render, redirect
from carros.models import Carro, Marca
from carros.forms import Carro_ModelForm
from django.views import View
from django.views.generic import ListView, CreateView

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

# class CadastraCarro(View):
#     def get(self, request):
#         novo_carro_form = Carro_ModelForm()
#         return render(request, 'cadastra_carro.html', {'novo_carro_form': novo_carro_form}) 

#     def post(self, request):
#         novo_carro_form = Carro_ModelForm(request.POST, request.FILES)
#         if novo_carro_form.is_valid():
#             novo_carro_form.save()
#             return redirect('index')
#         return render(request, 'cadastra_carro.html', {'novo_carro_form': novo_carro_form})

class CarroCreateView(CreateView):
    model = Carro
    form_class = Carro_ModelForm
    template_name = 'cadastra_carro.html'
    success_url = '/index/'
