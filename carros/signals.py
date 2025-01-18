from django.db.models.signals import pre_save, pre_delete, post_save, post_delete
from django.dispatch import receiver
from carros.models import Carro, CarroInventario
from django.db.models import Sum
from openai_api.client import carro_bio_cria

def carro_inventario_atualiza():
    carros_qtd = Carro.objects.all().count()
    carros_valor = Carro.objects.aggregate(total_value=Sum('valor'))['total_value']
    CarroInventario.objects.create(
        qtd = carros_qtd,
        valor = carros_valor
    )

    

@receiver(pre_save, sender=Carro)
def carro_pre_save(sender, instance, **kwargs):
    if not instance.bio:
        ai_bio = carro_bio_cria(instance.marca, instance.modelo, instance.ano_fabrica)
        instance.bio = ai_bio
        
@receiver(post_save, sender=Carro)
def carro_post_save(sender, instance, **kwargs):
    carro_inventario_atualiza()

# @receiver(pre_delete, sender=Carro)
# def carro_pre_delete(sender, instance, **kwargs):
#     print('### PRE DELETE ###')
#     print(instance)

@receiver(post_delete, sender=Carro)
def carro_post_delete(sender, instance, **kwargs):
    carro_inventario_atualiza()

    

