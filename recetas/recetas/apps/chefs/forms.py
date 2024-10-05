from django import forms
from .models import Chef

class RegistroChefForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña'}), max_length=100, required=True, error_messages={'required': 'Este campo es obligatorio'})
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirmar Contraseña'}), max_length=100, required=True, error_messages={'required': 'Este campo es obligatorio'})

    class Meta:
        model = Chef
        fields = ['tipo_documento', 'nombres', 'apellidos', 'email', 'celular', 'instagram', 'username', 'foto', 'password1', 'password2']
        error_messages = {
            'tipo_documento': {'required': 'Este campo es obligatorio'},
            'nombres': {'required': 'Este campo es obligatorio'},
            'apellidos': {'required': 'Este campo es obligatorio'},
            'email': {'required': 'Este campo es obligatorio'},
            'username': {'required': 'Este campo es obligatorio'},
            'celular': {'required': 'Este campo es obligatorio'},
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

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden")

        return cleaned_data

    def save(self, commit=True):
        chef = super().save(commit=False)
        chef.password = self.cleaned_data["password1"]
        if commit:
            chef.save()
        return chef