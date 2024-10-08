from django.urls import path, include
from django.contrib.auth.decorators import login_required

from apps.recetas.views import index, recetas_view, recetas_list, recetas_edit, recetas_delete, \
    RecetasList, RecetasCreate, RecetasUpdate, RecetasDelete, receta_detalle, receta_api_detail, recetas_api_list

urlpatterns = [
    path('', index, name='index'),
    path('nuevo/', login_required(RecetasCreate.as_view()), name='recetas_crear'),
    path('listar/', login_required(RecetasList.as_view()), name='recetas_listar'),
    path('editar/<pk>/', login_required(RecetasUpdate.as_view()), name='recetas_editar'),
    path('eliminar/<pk>/', login_required(RecetasDelete.as_view()), name='recetas_eliminar'),
    path('receta/<int:id>/', login_required(receta_detalle), name='receta_detalle'),
    path('recetas/', recetas_api_list, name='recetas_api_list'),
    path('recetas/<int:pk>/', receta_api_detail, name='receta_api_detail'),
]
