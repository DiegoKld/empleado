from django.contrib import admin
from .models import Empleado, Habilidades

# Register your models here.
admin.site.register(Habilidades)


#Modelar el administrador de django
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'first_name',
        'last_name',
        'departamento',
        'job',
        'full_name',
        
    )

    #Full name como tal no existe en el modelo empleados por lo que se debe crear la funcion para su funcionamiento
    #funcion decoradora
    def full_name(self, obj):
        
        return obj.first_name + '  ' + obj.last_name
    #
    search_fields = ('first_name',)#buscador 
    list_filter = ('job','habilidades')#filtrado por trabajo
    #Solo funciona para relaciones muchos a muchos
    filter_horizontal = ('habilidades',)

admin.site.register(Empleado, EmpleadoAdmin)