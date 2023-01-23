from django.shortcuts import render
# Vista generica que muestra html
from django.views.generic import (ListView)
from django.views.generic.edit import (FormView, CreateView)

#import bd

from .forms import NewDepartamentoForm
from applications.empleados.models import Empleado
from .models import Departamento

# Create your views here. or logic controller


class NewDepartamentoView(FormView):
    template_name = 'departamen/new_departamento.html'
    form_class = NewDepartamentoForm
    success_url = '/'

    def form_valid(self, form):

        print("Estamos en el form valid")

        depa = Departamento(
            name=form.cleaned_data['departamento'],
            short_name=form.cleaned_data['short_name']

        )
        depa.save()

        nombre = form.cleaned_data['nombre']
        apellido = form.cleaned_data['apellido']

        Empleado.objects.create(
            first_name=nombre,
            last_name=apellido,
            job='1',
            departamento=depa
        )

        return super(NewDepartamentoView, self).form_valid(form)

# Clase que lista departamentos


class DepartamentoListView(ListView):
    model = Departamento
    template_name = "departamen/lista.html"
    context_object_name = 'departamentos'
    paginate_by = 4
