from django.shortcuts import render
# importo reverse_lazy para que las urls permitan especificar urls de forma segura
from django.urls import reverse_lazy
# Vista generica que muestra html
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    TemplateView,
    UpdateView,
    DeleteView
)

# Create your views here. or logic controller

from .models import Empleado
# forms
from .form import EmpleadoForm
# Listar empleados


class InicioView(TemplateView):
    """Vista que carga la pagina inicio"""
    template_name = 'inicio.html'


class listAllEmpleados(ListView):
    template_name = 'empleados/list_all.html'
    paginate_by = 4

    def get_queryset(self):

        palabra_clave = self.request.GET.get("kword", '')
        lista = Empleado.objects.filter(
            # el icontains busca coincidencias dentro de lo que exista en palabra_clave. Se elige full name ya que siempre tiene un espacio intermedio
            full_name__icontains=palabra_clave
        )

        return lista


class listEmpleadosAdmin(ListView):
    template_name = 'empleados/list_empleados.html'
    paginate_by = 10
    ordering = 'first_name'
    context_object_name = 'empleados'
    model = Empleado

# Detalles del empleado


class empleadoDetailView(DetailView):
    model = Empleado
    template_name = "empleados/detail_empleados.html"

    def get_context_data(self, **kwargs):
        context = super(empleadoDetailView, self).get_context_data(**kwargs)
        context['titulo'] = 'Empleado del mes'
        return context


# Listar empleados por area


class listByAreaEmpleado(ListView):
    """Lista de empleados"""
    template_name = 'empleados/list_by_area.html'
    context_object_name = 'empleados'
    # este queryset hace que devuelva los empleados de un area especifica

    def get_queryset(self):

        filtro = self.kwargs['short_name']
        palabra_clave = self.request.GET.get('kword', '')
        if palabra_clave != '':
            lista = Empleado.objects.filter(
                full_name__icontains=palabra_clave
            )
            return lista
        else:
            lista = Empleado.objects.filter(
                departamento__short_name=filtro)
        return lista

        # esta es la forma en la que se recoge una variable de la url para ser procesada
        # area = self.kwargs['short_name']
        # lista = Empleado.objects.filter(
        #     departamento__name=area
        # )
        # return lista

# Listar empleados por palabra clave


class listEmpleadosbykword(ListView):
    """Lista empleados por palabra clave"""
    template_name = 'empleados/by_kword.html'
    # Re definir el nombre que nos va a devolver el listview
    context_object_name = 'empleados'
    # Funcion que permite captar y procesar lo que contiene la url

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')
        lista = Empleado.objects.filter(
            first_name=palabra_clave
        )

        return lista

# Listar habilidades por empleado


class listaHabilidadesByEmpleados(ListView):
    template_name = 'empleados/by_habilidades.html'
    context_object_name = 'habilidades'

    def get_queryset(self):
        # Funcion que permite captar y procesar lo que contiene la url
        id_habilidad = self.request.GET.get("id_persona", '')
        # recuperando un unico registro de la base de datos
        empleado = Empleado.objects.get(id=id_habilidad)

        return empleado.habilidades.all


class succesView(TemplateView):
    template_name = "empleados/succes.html"

# Con esta clase se evidencia como se ingresan cosas a la base de datos
# CreateView


class empleadoCreateView(CreateView):
    model = Empleado
    template_name = "empleados/add.html"
    form_class = EmpleadoForm
    # se debe especificar obligatoriamente una pagina que se cargue al momento de ejecutar el html
    # con ('__all__') se muestran todos, con['datoEspecifico']
    success_url = reverse_lazy('empleados_app:empleados_admin')
    # Funcion que acepta datos solo si son correctamente ingresados en  la solicitud de la vista

    def form_valid(self, form):
        # aca se generara y guardar el full name a partir del first_name y el last_name
        empleado = form.save()
        # print(empleado)
        # Ahora si se envia al modelo
        empleado.full_name = empleado.first_name + '  ' + empleado.last_name

        empleado.save()
        return super(empleadoCreateView, self).form_valid(form)

# Vista generica que nos permite actualizar registros


class EmpleadoUpdateView(UpdateView):
    template_name = "empleados/update.html"
    model = Empleado
    fields = [
        'first_name',
        'last_name',
        'job',
        'departamento',
        'habilidades',
    ]
    success_url = reverse_lazy('empleados_app:empleados_admin')

    def post(self, request, *args: str, **kwargs):
        self.object = self.get_object()
        # devuelve un diccionario por lo que podemos acceder a las claves
        print(request.POST)
        print(request.POST['last_name'])
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):

        return super(EmpleadoUpdateView, self).form_valid(form)


class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = "empleados/delete.html"
    success_url = reverse_lazy('empleados_app:empleados_admin')
