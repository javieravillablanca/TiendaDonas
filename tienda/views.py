from django.shortcuts import render, redirect
from .models import Categoria, Producto, Contact, Venta, DetalleVenta
from .forms import ContactForm, RegistroForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.db import transaction

# Create your views here.


@login_required
def agregar_producto(request, producto_id):
    if request.method == 'POST':
        carro = request.session.get('carro', [])
        producto = Producto.objects.get(id=producto_id)

        for item in carro:
            if item['id'] == producto_id:
                if item['cantidad'] < producto.stock:
                    item['cantidad'] += 1
                    item['total'] = item['precio'] * item['cantidad']
                    item['total2'] = item['precioEuro'] * item['cantidad']
                else:
                    
                    pass
                break
        else:
            if producto.stock > 0:
                carro.append({
                    'id': producto_id,
                    'categoria': producto.nombre,
                    'precio': producto.precio,
                    'precioEuro': producto.precioEuro,
                    'nombre': producto.nombre,
                    'src_image': producto.srcImagen,
                    'cantidad': 1,
                    'total': producto.precio * 1,
                    'total2': producto.precioEuro * 1
                })
            else:
                
                pass

        total_clp = sum(item['total'] for item in carro)
        total_euro = sum(item['total2'] for item in carro)

        request.session['carro'] = carro
        request.session['total_clp'] = total_clp
        request.session['total_euro'] = total_euro

        return redirect('ver_carrito')
    return redirect('ver_carrito')


@login_required
def ver_carrito(request): 
    carro = request.session.get('carro', [])
    total_clp = request.session.get('total_clp', 0)
    total_euro = request.session.get('total_euro', 0)

    return render(request, 'tienda/carrito.html', {'carro': carro, 'total_clp': total_clp, 'total_euro': total_euro})


@login_required
def finalizar(request):
    carrito = request.session.get("carro", [])
    if len(carrito) == 0:
        return redirect(to="index")

    with transaction.atomic():
        venta = Venta(usuario=request.user, total=sum(item["total"] for item in carrito))
        venta.save()

        for item in carrito:
            producto = Producto.objects.get(id=item["id"])
            cantidad_a_comprar = min(item["cantidad"], producto.stock)

            detalle = DetalleVenta(
                venta=venta,
                producto=producto,
                cantidad=cantidad_a_comprar,
                precio=item["precio"]
            )
            detalle.save()

            producto.stock -= cantidad_a_comprar
            producto.save()

    del request.session["carro"]
    return redirect(to="carrito")


@login_required
def borrar_producto(request, producto_id):
    if request.method == 'POST':
        carro = request.session.get('carro', [])
        carro = [item for item in carro if item['id'] != producto_id]

        total_clp = sum(item['total'] for item in carro)
        total_euro = sum(item['total2'] for item in carro)

        request.session['carro'] = carro
        request.session['total_clp'] = total_clp
        request.session['total_euro'] = total_euro

        return redirect('ver_carrito')
    return redirect('ver_carrito')


@login_required
def limpiar_carrito(request):
    if request.method == 'POST':
        request.session['carro'] = []
        request.session['total_clp'] = 0
        request.session['total_euro'] = 0
        return redirect('ver_carrito')
    return redirect('ver_carrito')


def registro(request):
    if request.method == 'POST':
        registro = RegistroForm(request.POST)
        if registro.is_valid():
            registro.save()
            return redirect(to='login')
    else:
        registro = RegistroForm()

    return render(request, 'tienda/registro.html', {'form': registro})


@login_required
def index(request):
    return render(request, 'tienda/index.html')


def inicio(request):
    return render(request, 'tienda/iniciodetodo.html')


@login_required
def carrito(request):
    return render(request, 'tienda/carrito.html')


@login_required
def admin(request):
    return render(request, 'tienda/index.html')


@login_required
def rellenas(request):
    productos = Producto.objects.filter(Categoria=1)

    for producto in productos:
        if producto.stock < 0:
            producto.stock = 0
            producto.save()

    contextRellenas = {"rellenas": productos}
    return render(request, 'tienda/rellenas.html', contextRellenas)


@login_required
def glaseadas(request):
    productos = Producto.objects.filter(Categoria=2).values()
    contextGlaseadas = {"glaseadas": productos}
    return render(request, 'tienda/glaseadas.html', contextGlaseadas)


@login_required
def bombon(request):
    productos = Producto.objects.filter(Categoria=3).values()
    contextBombon = {"bombon": productos}
    return render(request, 'tienda/bombon.html', contextBombon)


@login_required
def chispas(request):
    productos = Producto.objects.filter(Categoria=4).values()
    contextChispas = {"chispas": productos}
    return render(request, 'tienda/chispas.html', contextChispas)


@login_required
def nutella(request):
    productos = Producto.objects.filter(Categoria=5).values()
    contextNutella = {"nutella": productos}
    return render(request, 'tienda/nutella.html', contextNutella)


@login_required
def contact_view(request):
    contact_form = ContactForm()

    if request.method == 'POST':
        contact_form = ContactForm(data=request.POST)

        if contact_form.is_valid():
            contact_form.save()
            return redirect(reverse('Contact') + '?ok')
        else:
            return redirect(reverse('Contact') + '?error')

    messages = Contact.objects.all()

    return render(request, 'tienda/Contact.html', {'form': contact_form, 'messages': messages})
