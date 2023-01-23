from django.db import models
from applications.departamentos.models import Departamento

from ckeditor.fields import RichTextField


# Create your models here.


class Habilidades(models.Model):
    habilidad = models.CharField('Habilidad', max_length=50)

    class Meta:
        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidades empleado'

    def __str__(self):
        return str(self.id) + '  ' + self.habilidad


class Empleado(models.Model):
    JOB_CHOICES = (
        ('O', 'GERENTE'),
        ('1', 'COORDINADOR'),
        ('2', 'AUX ADMINISTRATIVO'),
        ('3', 'AUX SOPORTE'),
        ('4', 'AUX OPERATIVO'),
        ('5', 'CONDUCTOR'),
        ('6', 'SUPERVISOR'),
        ('7', 'SERVICIOS GENERALES'),
    )

    first_name = models.CharField('Nombres', max_length=50)
    last_name = models.CharField('Apellido', max_length=50)
    full_name = models.CharField(
        'Nombre completos',
        max_length=120,
        blank=True
    )
    job = models.CharField('Trabajo', max_length=50, choices=JOB_CHOICES)
    # Relaciono el modelo de departamento con el de empleados, relacion de uno a muchos
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='empleado', blank=True, null=True)
    #img = models.ImageField('', upload_to=None, height_field=None, width_field=None, max_length=None)

    # Relacion de muchos a muchos,
    habilidades = models.ManyToManyField(Habilidades)
    hoja_vida = RichTextField()

    class Meta:
        verbose_name = 'Mis empleados'
        verbose_name_plural = 'Empleados de la empresa'
        ordering = ['id']
        unique_together = ('first_name', 'last_name')  # que no se repita

    def __str__(self):
        return str(self.id) + '  ' + self.first_name + '  ' + self.last_name
