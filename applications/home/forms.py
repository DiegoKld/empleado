# Formularios en Django
from django import forms
from .models import Prueba
# mf y buscamos model forml en djaneiro y sale la estructura de la clas y buscamos model formle


class PruebaForm(forms.ModelForm):
    """Form definition for Prueba."""

    class Meta:
        """Meta definition for Pruebaform."""

        model = Prueba
        fields = (
            'titulo',
            'subtitulo',
            'cantidad',
        )

        widgets = {
            'titulo': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese texto aca'
                }
            )
        }

    def clean_cantidad(self):
        cantidad = self.cleaned_data['cantidad']
        if cantidad < 10:
            raise forms.ValidationError('Ingrese un subtitulo mayor a 10')

        return cantidad
