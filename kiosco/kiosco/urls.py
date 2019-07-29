"""kiosco URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from kiosco_app import views

from rest_framework import routers

from kiosco_app.views import ProductoViewSet, UserViewSet, ProveedorViewSet

router = routers.DefaultRouter()
router.register('producto', ProductoViewSet)
router.register('proveedor', ProveedorViewSet)
router.register('user', UserViewSet)




urlpatterns = [
    path('admin/', admin.site.urls),
    path('productos/', views.productos, name= 'productos_list'),
    path('productos/nuevo', views.producto_nuevo, name= 'productos_nuevo'),
    path('proveedores/', views.proveedores, name= 'proveedores_list'),
    path('proveedores/nuevo', views.proveedor_nuevo, name= 'proveedores_nuevo'),
    path('api/', include(router.urls)),
    ]
