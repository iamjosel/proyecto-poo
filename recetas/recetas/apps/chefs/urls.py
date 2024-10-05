from django.urls import path
from .views import RegistroChef, EditarChef, ListarChefs, VerChef, EliminarChef

urlpatterns = [
    path('registrar/', RegistroChef.as_view(), name="registrar"),
    path('listar/', ListarChefs.as_view(), name="chefs_listar"),
    path('editar/<int:pk>/', EditarChef.as_view(), name='editar_chef'),
    path('ver/<int:pk>/', VerChef.as_view(), name='ver_chef'),
    path('eliminar/<int:pk>/', EliminarChef.as_view(), name='eliminar_chef'),
]