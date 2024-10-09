from rest_framework import serializers
from apps.recetas.models import Recetas

class RecetasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recetas
        fields = ['id', 'receta', 'tipo', 'chef', 'pasos', 'ingredientes', 'descripcion', 'imagen']
