from django.urls import path
from apps.tipo.views import index_tipo, TipoList, TipoCreate, TipoUpdate, TipoDelete, TipoDetail, descripcion_list, descripcion_detail, receta_list, receta_detail

urlpatterns = [
    path('',  index_tipo, name='inicio'),
    path('tipo/listar', TipoList.as_view(), name='tipo_listar'),
    path('tipo/nueva', TipoCreate.as_view(), name='tipo_crear'),
    path('tipo/editar/<pk>/', TipoUpdate.as_view(), name='tipo_editar'),
    path('tipo/eliminar/<pk>/', TipoDelete.as_view(), name='tipo_eliminar'),
    path('tipo/detalle/<pk>/', TipoDetail.as_view(), name='tipo_detalle'),
    path('api/descripciones/', descripcion_list, name='descripcion_list'),
    path('api/descripciones/<int:pk>/', descripcion_detail, name='descripcion_detail'),
    path('api/recetas/', receta_list, name='receta_list'),
    path('api/recetas/<int:pk>/', receta_detail, name='receta_detail'),
]