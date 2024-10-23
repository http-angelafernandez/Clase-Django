from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from productos.models import Cuento
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class CrearCuento(LoginRequiredMixin, CreateView):
    model = Cuento
    template_name = "productos/crear_cuento.html"
    success_url = reverse_lazy('productos:listado_cuentos')
    fields = ['titulo', 'autor', 'fecha']

class ListadoCuentos(ListView):
    model = Cuento
    template_name = "productos/listado_cuentos.html"
    context_object_name = 'cuentos'

class VerCuento(DetailView):
    model = Cuento
    template_name = "productos/ver_cuento.html"

class EditarCuento(LoginRequiredMixin, UpdateView):
    model = Cuento
    template_name = "productos/editar_cuento.html"
    success_url = reverse_lazy('productos:listado_cuentos')
    fields = ['titulo', 'autor', 'fecha']

class EliminarCuento(LoginRequiredMixin, DeleteView):
    model = Cuento
    template_name = "productos/eliminar_cuento.html"
    success_url = reverse_lazy('productos:listado_cuentos')
    



