from django.db import models
from apps.tipo.models import Descripcion


class Recetas(models.Model):
    receta = models.CharField(max_length = 5000000)
    tipo = models.ForeignKey(Descripcion, null=True, blank=True, on_delete=models.CASCADE)
    pasos = models.CharField(max_length = 5000000)
    ingredientes = models.CharField(max_length = 5000000)
    descripcion = models.CharField(max_length = 5000000)
    imagen = models.ImageField(upload_to='recetas', null = True)







