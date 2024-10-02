from django.urls import path
from apps.tipo.views import index_tipo, TipoList, TipoCreate, TipoUpdate, TipoDelete, TipoDetail

urlpatterns = [
    path('',  index_tipo, name='inicio'),
    path('tipo/listar', TipoList.as_view(), name='tipo_listar'),
    path('tipo/nueva', TipoCreate.as_view(), name='tipo_crear'),
    path('tipo/editar/<pk>/', TipoUpdate.as_view(), name='tipo_editar'),
    path('tipo/eliminar/<pk>/', TipoDelete.as_view(), name='tipo_eliminar'),
    path('tipo/detalle/<pk>/', TipoDetail.as_view(), name='tipo_detalle'),
]