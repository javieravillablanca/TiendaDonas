# Generated by Django 5.0.6 on 2024-06-24 19:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(default='default', max_length=50)),
                ('definicion', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre y Apellido')),
                ('email', models.EmailField(max_length=100, unique=True, verbose_name='Correo Electrónico')),
                ('message', models.CharField(max_length=250, verbose_name='Mensaje')),
                ('contact_type', models.IntegerField(choices=[(0, 'Queja por un producto'), (1, 'Felicitaciones')], verbose_name='Tipo de contacto')),
                ('subscription', models.BooleanField(default=False, verbose_name='Suscribirme para más información')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de envío')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('stock', models.IntegerField(default=0)),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.TextField(default='Descripcion', max_length=200)),
                ('precio', models.IntegerField(null=True)),
                ('precioEuro', models.FloatField(default='0.0')),
                ('srcImagen', models.CharField(default='Imagen', max_length=400)),
                ('Categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tienda.categoria')),
            ],
        ),
    ]
