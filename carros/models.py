from django.db import models

class Marca(models.Model):
    id = models.AutoField(primary_key=True)
    marca = models.CharField(max_length=50)

    def __str__(self):
        return self.marca
    
    

class Carro(models.Model):
    id = models.AutoField(primary_key=True)
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT, related_name='marca_carro')
    modelo = models.CharField(max_length=200)
    ano_fabrica = models.IntegerField(blank=True, null=True)
    ano_modelo = models.IntegerField(blank=True, null=True)
    cor = models.CharField(max_length=50, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    placa = models.CharField(max_length=10, blank=True, null=True)
    valor = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    foto = models.ImageField(upload_to='carros/', blank=True, null=True)


    def __str__(self):
        return f'{self.modelo} - {self.ano_fabrica} - ID:{self.id}'
