from distutils.command.upload import upload
from django.db import models
from django.forms import ImageField
from applications.departamento.models import Departamento
from ckeditor.fields import RichTextField

# Create your models here.

class Habilidades(models.Model):
    habilidad = models.CharField('Habilidad', max_length=50)

    class Meta:
        verbose_name='Habilidad'
        verbose_name_plural='Habilidades' 

    def __str__(self):
        return str(self.id) + ' - ' + self.habilidad
    

class Empleado(models.Model):
    """ MODELO PARA CADA EMPLEADO """

    JOB_CHOICES = (
        ('0', 'Contador'),
        ('1', 'Administrador'),
        ('2', 'Economista'),
        ('3', 'Operaciones'),
        ('4', 'Proyectos'),
        ('5', 'Otro'),
    )
    # contador
    # administrador
    # Economista
    # otro
    first_name = models.CharField('Nombre', max_length=50)
    last_name = models.CharField('Apellidos', max_length=50)
    job = models.CharField('Trabajo', max_length=50, choices=JOB_CHOICES)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    #vatar = models.ImageField(upload_to='empleado', height_field=None, width_field=None, max_length=None)
    habilidades = models.ManyToManyField(Habilidades)
    hoja_vida = RichTextField()

    class Meta:
        verbose_name='Personal de la empresa'
        verbose_name_plural='Personal' 
        ordering = ['first_name']
        unique_together = ('first_name', 'last_name')

    def __str__(self):
        return str(self.id) + ' - ' + self.first_name + ' - ' + self.last_name
