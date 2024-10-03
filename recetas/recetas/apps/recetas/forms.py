from django import forms
from apps.recetas.models import Recetas

class RecetasForm(forms.ModelForm):

    class Meta:
        model = Recetas

        fields = [
            'receta',
            'tipo',
            'chef',
            'pasos',
            'ingredientes',
            'descripcion',
            'imagen',

        ]
        labels = {
            'receta': 'Nombre receta',
            'tipo': 'Tipo de receta',
            'chef': 'Dueño de la receta',
            'pasos':'Pasos para preparar la receta',
            'ingredientes':'Ingredientes',
            'descripcion':'Descripcion de la receta',
            'imagen':'Imagen de la receta',

        }
        widgets = {
            'receta': forms.TextInput(attrs={'class':'form-control'}),
            'tipo': forms.Select(attrs={'class:': 'form-control'}),
            'chef': forms.Select(attrs={'class:': 'form-control'}),
            'pasos': forms.Textarea(attrs={'class': 'form-control'}),
            'ingredientes': forms.Textarea(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
            'imagen': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
