from django.urls import path
from django.contrib.auth.views import LoginView
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('index', views.index, name='index'),
    path('admin/', views.admin, name='admin'),
    path('carrito/', views.carrito, name='carrito'),
    path('rellenas/', views.rellenas, name='rellenas'),
    path('glaseadas/', views.glaseadas, name='glaseadas'),
    path('bombon/', views.bombon, name='bombon'),
    path('chispas/', views.chispas, name='chispas'),
    path('nutella/', views.nutella, name='nutella'),
    path('contact/', views.contact_view, name='Contact'),
    path('login/',LoginView.as_view(template_name='tienda/login.html'),name="login"),
    path('registro/', views.registro, name='registro'),
    path('agregar_producto/<producto_id>/', views.agregar_producto, name='agregar_producto'),
    path('borrar_producto/<producto_id>/', views.borrar_producto, name='borrar_producto'),
    path('limpiar/', views.limpiar_carrito, name='limpiar_carrito'),
    path('ver_carrito/', views.ver_carrito, name='ver_carrito'),
    path('finalizar',views.finalizar , name= "finalizar"),
    
]




 