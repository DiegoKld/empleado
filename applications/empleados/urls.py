from django.urls import path
# vistas importadas
from . import views

app_name = "empleados_app"

urlpatterns = [
    path(
        '',
        views.InicioView.as_view(),
        name='inicio'
    ),

    path(
        'listar-empleados/',
        views.listAllEmpleados.as_view(),
        name='empleados-all'),

    path(
        'listar-by-area/<short_name>/',
        views.listByAreaEmpleado.as_view(),
        name='empleados_all'
    ),

    path(
        'lista-empleados-admin/',
        views.listEmpleadosAdmin.as_view(),
        name='empleados_admin'
    ),

    path(
        'buscar-empleado/',
        views.listEmpleadosbykword.as_view()
    ),

    path('lista-habilidades-empleados/',
         views.listaHabilidadesByEmpleados.as_view()),

    # pk hace referencia al id que se crea por defecto en el modelo
    path(
        'ver-empleados/<pk>/',
        views.empleadoDetailView.as_view(),
        name='empleado_detail',

    ),

    path(
        'succes-empleado/',
        views.succesView.as_view(),
        name='correcto'
    ),

    path(
        'add-empleado/',
        views.empleadoCreateView.as_view(),
        name='empleado_add'
    ),

    path(
        'update-empleado/<pk>/',
        views.EmpleadoUpdateView.as_view(),
        name='modificar_empleado'
    ),

    path(
        'delete-empleado/<pk>/',
        views.EmpleadoDeleteView.as_view(),
        name='eliminar_empleado'
    ),

]
