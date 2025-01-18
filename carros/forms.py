from django import forms
from carros.models import Marca, Carro

class Carro_ModelForm(forms.ModelForm):
    class Meta:
        model = Carro
        fields = '__all__'

    def clean_valor(self):
        valor = self.cleaned_data.get('valor')
        if valor < 20000:
            self.add_error('valor', 'O valor do carro deve ser maior que R$ 20.000')
        return valor


    