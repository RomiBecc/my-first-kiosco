from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import FormView
from django.views.generic import ListView
#from rest_framework import viewsets
#from rest_framework.permissions import AllowAny

from .forms import ProductoForm
from .models import Producto



class ProductoListView(ListView):
    model = Producto
    template_name = "kiosco_app/producto_list.html"

class ProductoFormView(FormView):
    form_class = ProductoForm
    success_url = reverse_lazy('productos_list')
    template_name = "kiosco_app/producto_nuevo.html"


productos = ProductoListView.as_view()

