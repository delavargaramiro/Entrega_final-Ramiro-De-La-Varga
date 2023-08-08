from datetime import datetime
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from .models import Avatar, Cliente, Producto, Pedido
from .forms import ClienteForm, PedidoForm, ProductoForm, BusquedaForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm




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

    context = {'form': form}
    return render(request, 'app/pedido_form.html', context)

def lista_pedidos(request):
    pedidos = Pedido.objects.all()
    return render(request, 'app/lista_pedidos.html', {'pedidos': pedidos})

def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'app/lista_clientes.html', {'clientes': clientes})

def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'app/lista_productos.html', {'productos': productos})

def editar_cliente(request, cliente_id):
    cliente = Cliente.objects.get(id=cliente_id)
    
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('lista_clientes')
    else:
        form = ClienteForm(instance=cliente)
    
    return render(request, 'app/cliente_editar.html', {'form': form})


def borrar_cliente(request, cliente_id):
    cliente = Cliente.objects.get(id=cliente_id)
    
    if request.method == 'POST':
        cliente.delete()
        return redirect('lista_clientes')
    
    return render(request, 'app/cliente_borrar.html', {'cliente': cliente})

def editar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'app/editar_producto.html', {'form': form, 'producto': producto})

def borrar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        producto.delete()
        return redirect('lista_productos')
    return render(request, 'app/borrar_producto.html', {'producto': producto})

def editar_pedido(request, pedido_id):
    pedido = get_object_or_404(Pedido, pk=pedido_id)
    if request.method == 'POST':
        form = PedidoForm(request.POST, instance=pedido)
        if form.is_valid():
            form.save()
            return redirect('lista_pedidos')
    else:
        form = PedidoForm(instance=pedido)
    return render(request, 'app/editar_pedido.html', {'form': form})

def borrar_pedido(request, pedido_id):
    pedido = get_object_or_404(Pedido, pk=pedido_id)
    if request.method == 'POST':
        pedido.delete()
        return redirect('lista_pedidos')
    return render(request, 'app/borrar_pedido.html', {'pedido': pedido})
#____________

def login_request(request):
    mensaje = ""
    if request.method == "POST":
        miForm = AuthenticationForm(request, data=request.POST)
        if miForm.is_valid():
            usuario = miForm.cleaned_data.get('username')
            clave = miForm.cleaned_data.get('password')
            user = authenticate(username=usuario, password=clave)
            if user is not None:
                login(request, user)

                try:
                    avatar = Avatar.objects.get(user=request.user.id).imagen.url
                except Avatar.DoesNotExist:
                    avatar = '/media/avatares/default.png'
                
                request.session['avatar'] = avatar

                return render(request, "app/index.html", {"mensaje": f"Bienvenido {usuario}"})
            else:
                return render(request, "app/login.html", {"form": miForm, "mensaje": "Datos Inválidos"})
        else:
            return render(request, "app/login.html", {"form": miForm, "mensaje": "Datos Inválidos"})

    miForm = AuthenticationForm()
    return render(request, "app/login.html", {"form": miForm})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('Home')  # Cambia 'Home' con la URL a la que quieres redirigir al usuario después de iniciar sesión
    else:
        form = AuthenticationForm()
    return render(request, 'app/login.html', {'form': form})

def registro_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            form.save()
            return render(request, "app/index.html", {"mensaje":"Usuario Creado"})        
    else:
        form = UserCreationForm()
    return render(request, 'app/registro.html', {'form': form})



def logout_view(request):
    logout(request)
    return redirect('Home')  # Cambia 'Home' con la URL a la que quieres redirigir al usuario después de cerrar sesión