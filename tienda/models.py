from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.

class Categoria(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre=models.CharField(default="default", max_length=50)
    definicion=models.TextField(blank=True)
    def __str__(self):
        return self.nombre
    


class Producto(models.Model):
    id = models.IntegerField(primary_key=True)
    stock = models.IntegerField(default=1)
    nombre =models.CharField(max_length=50)
    precio=models.IntegerField(null=True)
    precioEuro=models.FloatField(default="0.0")
    Categoria=models.ForeignKey(Categoria,on_delete=models.CASCADE)
    srcImagen = models.CharField(default="Imagen",max_length=400)
    def __str__(self):
        return self.nombre
    



class Contact(models.Model):
    name= models.CharField(max_length= 50, verbose_name="Nombre y Apellido")
    email=models.EmailField(unique=True,max_length=100, verbose_name="Correo Electrónico")
    message=models.CharField(max_length=250, verbose_name="Mensaje")
    options = [
    [0, 'Queja por un producto'],
    [1, 'Felicitaciones']

]
    contact_type = models.IntegerField(choices=options, verbose_name="Tipo de contacto")
    subscription = models.BooleanField(default=False, verbose_name= "Suscribirme para más información")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de envío')
    
    

      


    def __str__(self) :
        return self.name 
    



class Venta(models.Model):
    usuario = models.ForeignKey(to=User, on_delete = models.CASCADE)
    fecha = models.DateTimeField(default=datetime.now, blank=True)
    total = models.IntegerField()

    def __str__(self):
        return f"{self.id} {self.usuario.username} {self.fecha}"

class DetalleVenta(models.Model):
    producto = models.ForeignKey(to=Producto, on_delete=models.CASCADE)
    venta = models.ForeignKey(to=Venta, on_delete=models.CASCADE)
    precio = models.IntegerField()
    cantidad = models.IntegerField()

    def __str__(self):
        return f"{self.venta.id} { self.producto.nombre}"
