from django.db import models
from apps.tipo.models import Descripcion
from apps.chefs.models import Chef

class Recetas(models.Model):
    receta = models.CharField(max_length=255)
    tipo = models.ForeignKey(Descripcion, null=True, on_delete=models.CASCADE)
    chef = models.ForeignKey(Chef, null=True, on_delete=models.CASCADE)
    pasos = models.TextField()
    ingredientes = models.TextField()
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='recetas', null=True, blank=False)

    def __str__(self):
        return self.receta