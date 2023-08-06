from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Cliente, Producto, Pedido
from .forms import ClienteForm, PedidoForm, ProductoForm, BusquedaForm



def index(request):
    return render(request, "app/index.html")

def sobremi(request):
    return render(request, "app/sobremi.html")

def cliente_view(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('clientes')
    else:
        form = ClienteForm()
    return render(request, 'app/cliente_form.html', {'form': form})

def producto_view(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('producto')
    else:
        form = ProductoForm()
    return render(request, 'app/producto_form.html', {'form': form})

def buscar_view(request):
    if request.method == 'POST':
        form = BusquedaForm(request.POST)
        if form.is_valid():
            termino_busqueda = form.cleaned_data['termino_busqueda']
            resultados_clientes = Cliente.objects.filter(nombre__icontains=termino_busqueda)
            resultados_productos = Producto.objects.filter(nombre__icontains=termino_busqueda)
            resultados_pedidos = Pedido.objects.filter(cliente__nombre__icontains=termino_busqueda) | Pedido.objects.filter(producto__nombre__icontains=termino_busqueda)
            return render(request, 'app/resultados_busqueda.html', 
                          {'resultados_clientes': resultados_clientes, 'resultados_productos': resultados_productos, 'resultados_pedidos': resultados_pedidos,})
    else:
        form = BusquedaForm()
    return render(request, 'app/buscar_form.html', {'form': form})

def pedido_view(request):
    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            pedido = form.save(commit=False)  
            pedido.total = pedido.cantidad * pedido.producto.precio
            fecha_actual = datetime.now().date() 
            pedido.fecha_pedido = fecha_actual
            pedido.save()  
            return redirect('pedido') 
    else:
        form = PedidoForm()
    return render(request, 'app/pedido_form.html', {'form': form})


def lista_pedidos(request):
    pedidos = Pedido.objects.all()
    return render(request, 'app/lista_pedidos.html', {'pedidos': pedidos})

def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'app/lista_clientes.html', {'clientes': clientes})

def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'app/lista_productos.html', {'productos': productos})

