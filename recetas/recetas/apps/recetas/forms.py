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
            'receta': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'ejemplo: Tarta de Manzana'}),
            'tipo': forms.Select(attrs={'class:': 'form-control', 'placeholder': 'ejemplo: Postre'}),
            'chef': forms.Select(attrs={'class:': 'form-control', 'placeholder': 'ejemplo: Salt Bae'}),
            'pasos': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'ejemplo: 1. Precalentar el horno a 180°C.\n2. Pelar y cortar las manzanas.\n3. Mezclar las manzanas con azúcar y canela.\n4. Colocar la mezcla en una base de masa.\n5. Hornear durante 45 minutos.'}),
            'ingredientes': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'ejemplo: 1. 4 manzanas\n2. 200g de azúcar\n3. 1 cucharadita de canela\n4. Masa para tarta'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'ejemplo: Una deliciosa tarta de manzana con un toque de canela, perfecta para el postre.'}),
            'imagen': forms.ClearableFileInput(attrs={'class': 'form-control', 'placeholder': 'ejemplo: tarta_manzana.jpg'}),
        }