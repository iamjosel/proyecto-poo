from django import forms
from apps.tipo.models import Descripcion, Receta

class DescripcionForm(forms.ModelForm):

    class Meta:
        model = Descripcion
        fields = [
            'nombre',

        ]
        labels = {
            'nombre': 'Tipo de receta: ',
        }
        widgets = {
        }

class RecetaForm(forms.ModelForm):

    class Meta:
        model = Receta
        fields = [
        ]
