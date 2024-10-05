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
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ejemplo: Postre'}),
        }

class RecetaForm(forms.ModelForm):

    class Meta:
        model = Receta
        fields = [
        ]
