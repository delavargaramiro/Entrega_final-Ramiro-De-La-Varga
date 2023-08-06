from django.urls import path, include
from .views import *
from . import views

urlpatterns = [
    path("", index, name="Home"),
    path("sobremi/", sobremi, name="sobremi"),
    path('cliente/', views.cliente_view, name="clientes"),
    path('producto/', views.producto_view, name="producto"),
    path('buscar/', buscar_view, name="buscar"),
    path('pedido/', views.pedido_view, name="pedido"),
    path('pedidos/', views.lista_pedidos, name="lista_pedidos"),
    path('clientes/', views.lista_clientes, name="lista_clientes"),
    path('productos/', views.lista_productos, name="lista_productos"),
    ]