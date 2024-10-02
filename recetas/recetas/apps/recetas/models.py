from django.db import models
from apps.tipo.models import Descripcion


class Recetas(models.Model):
    receta = models.CharField(max_length = 5000)
    tipo = models.ForeignKey(Descripcion, null=True, on_delete=models.CASCADE)
    pasos = models.CharField(max_length = 5000)
    ingredientes = models.CharField(max_length = 5000)
    descripcion = models.CharField(max_length = 5000)
    imagen = models.ImageField(upload_to='recetas', null = True)