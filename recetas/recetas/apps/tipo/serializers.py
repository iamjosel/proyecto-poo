from rest_framework import serializers
from .models import Descripcion, Receta

class DescripcionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Descripcion
        fields = '__all__'

class RecetaSerializer(serializers.ModelSerializer):
    descripcion = DescripcionSerializer()  # Para incluir el detalle de la descripción

    class Meta:
        model = Receta
        fields = ['nombre',]
