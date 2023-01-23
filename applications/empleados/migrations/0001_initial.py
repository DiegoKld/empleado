# Generated by Django 4.0.4 on 2023-01-16 01:22

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('departamentos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Habilidades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('habilidad', models.CharField(max_length=50, verbose_name='Habilidad')),
            ],
            options={
                'verbose_name': 'Habilidad',
                'verbose_name_plural': 'Habilidades empleado',
            },
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='Nombres')),
                ('last_name', models.CharField(max_length=50, verbose_name='Apellido')),
                ('full_name', models.CharField(blank=True, max_length=120, verbose_name='Nombre completos')),
                ('job', models.CharField(choices=[('O', 'GERENTE'), ('1', 'COORDINADOR'), ('2', 'AUX ADMINISTRATIVO'), ('3', 'AUX SOPORTE'), ('4', 'AUX OPERATIVO'), ('5', 'CONDUCTOR'), ('6', 'SUPERVISOR'), ('7', 'SERVICIOS GENERALES')], max_length=50, verbose_name='Trabajo')),
                ('hoja_vida', ckeditor.fields.RichTextField()),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='departamentos.departamento')),
                ('habilidades', models.ManyToManyField(to='empleados.habilidades')),
            ],
            options={
                'verbose_name': 'Mis empleados',
                'verbose_name_plural': 'Empleados de la empresa',
                'ordering': ['id'],
                'unique_together': {('first_name', 'last_name')},
            },
        ),
    ]
