from django.contrib import admin
from .models import Producto, Proveedor, Ingreso, Egreso

#admin.site.register(Producto) #permite visualizar los productos en el admin
admin.site.register(Proveedor)
admin.site.register(Ingreso)
admin.site.register(Egreso)

class ProductoAdmin(admin.ModelAdmin):
    list_filter = ['codigo_producto']

admin.site.register(Producto, ProductoAdmin)

