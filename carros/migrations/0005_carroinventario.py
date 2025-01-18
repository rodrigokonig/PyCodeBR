# Generated by Django 5.1.5 on 2025-01-18 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carros', '0004_carro_foto_carro_placa'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarroInventario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qtd', models.IntegerField()),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10)),
                ('data_atualizacao', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-data_atualizacao'],
            },
        ),
    ]