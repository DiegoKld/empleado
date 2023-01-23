from django.shortcuts import render
from django.views.generic import (ListView)

#from empleados.applications.departamento.models import Departamento

from .models import Empleado


class ListAllEmpleados(ListView):
    template_name = 'persona/list_all.html'
    model = Empleado
    #context_object_name = 'lista'


class ListByAreaEmpleado(ListView):
    """ Lista empleados de un area """

    template_name = 'persona/list_by_area.html'
    queryset = Empleado.objects.filter(
        departamento__name='Contabilidad'
    )
    #context_object_name = 'lista'
