from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Producto, Proveedor, Ingreso, Egreso

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = [
            'nombre',
            'descripcion',
            'codigo_producto',
            'precio_sugerido',
        ]
class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = [
            'nombre',
            'cuit',
            'direccion',
            'telefono',
        ]
class UserSerializer(serializers.ModelSerializer):
    productos = ProductoSerializer(many=True, source="producto_set")
    proveedores = ProveedorSerializer(many= True, source= "proveedor_set")
    custom_field = serializers.SerializerMethodField()

    class Meta:
        model = User
        fiels = [
            'productos',
            'proveedores',
            'custom_field'
        ]