from django.urls import path, include
from .views import *
from . import views
from django.contrib.auth.views import LogoutView


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
    path('editar_cliente/<int:cliente_id>/', views.editar_cliente, name='editar_cliente'),
    path('borrar_cliente/<int:cliente_id>/', views.borrar_cliente, name='borrar_cliente'),
    path('productos/<int:pk>/editar/', views.editar_producto, name='editar_producto'),
    path('productos/<int:pk>/borrar/', views.borrar_producto, name='borrar_producto'),
    path('editar_pedido/<int:pedido_id>/', views.editar_pedido, name='editar_pedido'),
    path('borrar_pedido/<int:pedido_id>/', views.borrar_pedido, name='borrar_pedido'),
    path('login/', views.login_view, name='login'),
    path('registro/', views.registro_view, name='registro'),
    path('logout/', LogoutView.as_view(template_name="app/logout.html"), name="logout"),



    ]