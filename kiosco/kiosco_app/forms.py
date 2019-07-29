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

class IngresoForm(forms.ModelForm):

    class Meta:
        model = Ingreso
        fields = ('producto','proveedor','cantidad','fecha')


class EgresoForm(forms.ModelForm):
    class Meta:
        model = Egreso
        fields = ('producto', 'cantidad', 'fecha')

    def clean_cantidad(self):
        cantidad = self.cleaned_data['cantidad']
        producto = self.cleaned_data['producto']
        if producto.get_stock() < cantidad:
            raise forms.ValidationError(f"La cantidad solicitada({cantidad}) es mayor al stock. Su stock actual es {producto.get_stock()}.")
        return cantidad

