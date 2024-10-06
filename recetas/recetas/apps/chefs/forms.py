from django import forms
from .models import Chef

class RegistroChefForm(forms.ModelForm):
    class Meta:
        model = Chef
        fields = ['tipo_documento', 'nombres', 'apellidos', 'email', 'celular', 'instagram', 'username', 'foto']
        error_messages = {
            'tipo_documento': {'required': 'Este campo es obligatorio'},
            'nombres': {'required': 'Este campo es obligatorio'},
            'apellidos': {'required': 'Este campo es obligatorio'},
            'email': {'required': 'Este campo es obligatorio'},
            'username': {'required': 'Este campo es obligatorio'},
            'celular': {'required': 'Este campo es obligatorio'},
        }
        labels = {
            'tipo_documento': 'Tipo Documento:',
            'nombres': 'Nombres:',
            'apellidos': 'Apellidos:',
            'email': 'Correo Electrónico:',
            'celular': 'Número de Celular:',
            'instagram': 'Instagram:',
            'username': 'Username:',
            'foto': 'Foto:',
        }
        widgets = {
            'tipo_documento': forms.Select(attrs={'class': 'form-control', 'placeholder': 'ejemplo: Cédula de Ciudadanía'}),
            'nombres': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ejemplo: Lionel'}),
            'apellidos': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ejemplo: Messi'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'ejemplo: lionel@messi.com'}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ejemplo: lionelmessi'}),
            'instagram': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ejemplo: @liomessi'}),
            'celular': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ejemplo: 3123123132'}),
            'foto': forms.FileInput(attrs={'class': 'form-control'}),
        }