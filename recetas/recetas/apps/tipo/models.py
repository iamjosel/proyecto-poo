from django.db import models

class Descripcion(models.Model):
    nombre = models.CharField(max_length=255)  # Cambié a 255 para un tamaño estándar de texto

    def __str__(self):
        return self.nombre

class Receta(models.Model):
    descripcion = models.ForeignKey(Descripcion, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'Receta #{self.id} - {self.descripcion.nombre}'