from django.contrib import admin
from .models import Empleado, Habilidades

# Register your models here.

admin.site.register(Habilidades)


class EmpleadoAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'departamento',
        'job',
        # voy  a mostrar una columna que no esta en el modelo
        'full_name',
    )

    # Para que funcione el full_name debo crear una funcion que le de valor
    def full_name(self, obj):
        return obj.first_name + ' ' + obj.last_name

    # Incluir buscador
    search_fields = ('first_name',)
    # agregar filtrador
    list_filter = ('departamento', 'job', 'habilidades', )
    filter_horizontal = ('habilidades',)


admin.site.register(Empleado, EmpleadoAdmin)
