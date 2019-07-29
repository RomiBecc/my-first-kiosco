from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.utils import timezone

from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from django.views.generic import FormView
from django.views.generic import ListView
from .forms import ProductoForm, ProveedorForm
from .models import Producto, Proveedor, Ingreso, Egreso
from .serializers import ProductoSerializer, UserSerializer, ProveedorSerializer


class ProductoListView(ListView):
    model = Producto
    template_name = "kiosco_app/producto_list.html"

    def get_queryset(self):
        queryset = super(ProductoListView, self).get_queryset()
        queryset = queryset.order_by("-id")
        return queryset


class ProductoFormView(FormView):
    form_class = ProductoForm

    success_url = reverse_lazy('productos_list')
    template_name = "kiosco_app/producto_edit.html"

    def form_valid(self, form):
        producto = form.save(commit=False)
        producto.save()
        return super(ProductoFormView, self).form_valid(form)

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().prefetch_related(
        "producto_set",
        "proveedor_set"
    )
    serializer_class = UserSerializer


class ProveedorListView(ListView):
    model = Proveedor
    template_name = "kiosco_app/proveedores_list.html"

    def get_queryset(self):
        queryset = super(ProveedorListView, self).get_queryset()
        queryset = queryset.order_by("-id")
        return queryset


class ProveedorFormView(FormView):
    form_class = ProveedorForm

    success_url = reverse_lazy('proveedores_list')
    template_name = "kiosco_app/proveedor_edit.html"

    def form_valid(self, form):
        proveedor = form.save(commit=False)
        proveedor.save()
        return super(ProveedorFormView, self).form_valid(form)

class ProveedorViewSet(viewsets.ModelViewSet):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer

proveedor_nuevo = login_required(ProveedorFormView.as_view(), login_url="/admin/login")
proveedores = ProveedorListView.as_view()



producto_nuevo= login_required(ProductoFormView.as_view(), login_url="/admin/login")
productos = ProductoListView.as_view()

