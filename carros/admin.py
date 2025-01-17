from django.contrib import admin
from carros.models import Carro, Marca


class MarcasAdmin(admin.ModelAdmin):
    list_display = ('id', 'marca')
    search_fields = ('marca',)


class CarrosAdmin(admin.ModelAdmin):
    list_display = ('id', 'modelo', 'marca', 'ano_fabrica', 'ano_modelo', 'cor', 'valor')
    search_fields = ('modelo', 'marca')


admin.site.register(Carro, CarrosAdmin)
admin.site.register(Marca, MarcasAdmin)

