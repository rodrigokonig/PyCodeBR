from django import forms
from carros.models import Marca, Carro

class CarroForm(forms.Form):
    marca = forms.ModelChoiceField(Marca.objects.all())
    modelo = forms.CharField(max_length=200)
    ano_fabrica = forms.IntegerField()
    ano_modelo = forms.IntegerField()
    cor = forms.CharField()
    bio = forms.CharField()
    placa = forms.CharField(max_length=10)
    valor = forms.DecimalField(max_digits=10)
    foto = forms.ImageField()

    def save(self):
        carro = Carro(
            modelo = self.cleaned_data['modelo'],
            ano_fabrica = self.cleaned_data['ano_fabrica'],
            ano_modelo = self.cleaned_data['ano_modelo'],
            cor = self.cleaned_data['cor'],
            bio = self.cleaned_data['bio'],
            placa = self.cleaned_data['placa'],
            valor = self.cleaned_data['valor'],
            foto = self.cleaned_data['foto'],
            marca = self.cleaned_data['marca']
        )
        carro.save()
        return carro

