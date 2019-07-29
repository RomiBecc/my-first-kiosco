from django import forms
from .models import Producto, Proveedor, Ingreso, Egreso

class ProductoForm(forms.ModelForm):

    class Meta:
        model = Producto
        fields= ('codigo_producto', 'nombre','descripcion', 'precio_sugerido')


class ProveedorForm(forms.ModelForm):

    class Meta:
        model= Proveedor
        fields = ('nombre','cuit','direccion','telefono')