from django.shortcuts import render
# Vista generica que muestra html
from django.views.generic import (TemplateView, ListView, CreateView)

#import bd
from .models import Prueba
from .forms import PruebaForm

# Create your views here. or logic controller


class IndexView(TemplateView):
    template_name = 'home/home.html'


class PruebaListviwe(ListView):
    template_name = 'home/lista.html'
    queryset = ['A', 'B', 'C']
    context_object_name = 'listaPrueba'


class ModeloPruebaListView(ListView):
    model = Prueba
    template_name = "home/pruebas.html"
    context_object_name = 'listaPrueba'


class PruebaCreateView(CreateView):
    model = Prueba
    template_name = "home/add.html"
    # reemplazo los field por form_class ya que los field estan implicitos en esta clase
    form_class = PruebaForm
    success_url = '/'


class ResumeFoundationView(TemplateView):
    template_name = "home/resume_foundation.html"
