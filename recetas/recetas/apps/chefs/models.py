from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone

def validate_only_letters(value):
    if not value.isalpha():
        raise ValidationError('Este campo solo puede contener letras.')

def validate_only_numbers(value):
    if not value.isdigit():
        raise ValidationError('Este campo solo puede contener números.')

class Chef(models.Model):
    TIPO_DOCUMENTO_CHOICES = [
        ('CC', 'Cédula de Ciudadanía'),
        ('PAS', 'Pasaporte'),
    ]

    tipo_documento = models.CharField(max_length=5, choices=TIPO_DOCUMENTO_CHOICES, blank=False)
    nombres = models.CharField(max_length=70, blank=False, validators=[validate_only_letters])
    apellidos = models.CharField(max_length=70, blank=False, validators=[validate_only_letters])
    email = models.EmailField(max_length=100, blank=False)
    username = models.CharField(max_length=70, blank=False)
    celular = models.CharField(max_length=10, blank=False, validators=[validate_only_numbers])
    instagram = models.CharField(max_length=100, blank=True)
    foto = models.ImageField(upload_to='chefs_fotos/', blank=False, null=False)

    def __str__(self):
        return f'{self.nombres} {self.apellidos}'