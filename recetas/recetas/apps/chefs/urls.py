from django.urls import path, include
from .views import RegistroChef, ListarChefs

urlpatterns = [
    path('registrar/', RegistroChef.as_view(), name="registrar"),
    path('listar/', ListarChefs.as_view(), name="chefs_listar"),
]