from django import forms
from apps.recetas.models import Recetas

class RecetasForm(forms.ModelForm):
    class Meta:
        model = Recetas
        fields = ['receta', 'tipo', 'chef', 'pasos', 'ingredientes', 'descripcion', 'imagen']
        
        labels = {
            'receta': 'Nombre de la receta',
            'tipo': 'Tipo de receta',
            'chef': 'Chef responsable',
            'pasos': 'Pasos para preparar la receta',
            'ingredientes': 'Ingredientes',
            'descripcion': 'Descripción de la receta',
            'imagen': 'Imagen de la receta',
        }

        widgets = {
            'receta': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ejemplo: Tarta de Manzana'}),
            'tipo': forms.Select(attrs={'class': 'form-control'}),
            'chef': forms.Select(attrs={'class': 'form-control'}),
            'pasos': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Describa los pasos...'}),
            'ingredientes': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'ejemplo: 1. 4 manzanas, etc.'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Breve descripción de la receta'}),
            'imagen': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }