from datetime import date
import formatter
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    direccion = models.CharField(max_length=200)
    email = models.EmailField()
    tarjeta_credito = models.CharField(max_length=16)
    saldo = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre
    
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad = models.IntegerField()
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre
    
@property
def precio_con_simbolo(self):
        return f"${formatter.number_format(self.precio, decimal_pos=2)}"

class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    total = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_pedido = models.DateField(default=date(2023, 1, 1))

    def __str__(self):
        return f"Pedido de {self.cantidad} {self.producto} de {self.cliente}"
    
class Avatar(models.Model):
    imagen = models.ImageField(upload_to="avatares")
    user = models.ForeignKey(User, on_delete= models.CASCADE)

    def __str__(self):
        return f"{self.user} [{self.imagen}]"