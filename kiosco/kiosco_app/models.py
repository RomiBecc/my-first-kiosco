from django.db import models
from django.utils import timezone
# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.TextField()
    codigo_producto= models.CharField('Codigo de Producto', max_length=100, unique=True)
    precio_sugerido= models.DecimalField(max_digits=10, decimal_places=2)

    def guardar(self):
        self.save()

    def eliminar(self):
        self.delete()

    def __str__(self):
        return self.nombre
#devuelve el stock
    def get_stock(self):
        return  self.ingreso()-self.egreso()

#devuelve todos los ingresos del producto
    def ingreso(self):
        return sum(self.ingreso_set.values_list('cantidad', flat=True))
#devuelve todos los egresos del producto
    def egreso(self):
        return sum(self.egreso_set.values_list('cantidad', flat=True))

class Proveedor(models.Model):
    nombre = models.CharField(max_length=50)
    cuit = models.BigIntegerField(unique=True)
    direccion = models.CharField(max_length=150)
    telefono = models.CharField(max_length=20)

    def guardar(self):
        self.save()

    def __str__(self):
        return self.nombre

class Ingreso(models.Model):
    producto = models.ForeignKey('kiosco_app.Producto', on_delete= models.CASCADE)
    proveedor= models.ForeignKey('kiosco_app.Proveedor', on_delete= models.CASCADE)
    fecha = models.DateTimeField(default=timezone.now)
    cantidad = models.PositiveIntegerField()

    def guardar(self):
        self.save()

    def __str__(self):
        return f"Producto: {self.producto.__str__()}, Proveedor: {self.proveedor.__str__()}, Cantidad:{self.cantidad}"




class Egreso(models.Model):
    producto = models.ForeignKey('kiosco_app.Producto', on_delete=models.CASCADE)
    fecha = models.DateTimeField(default=timezone.now)
    cantidad = models.PositiveIntegerField()

    def guardar(self):
        self.save()

    def __str__(self):
        return f"Producto: {self.producto.__str__()}, Cantidad:{self.cantidad}"

