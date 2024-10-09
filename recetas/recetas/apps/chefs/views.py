from django.views.generic import UpdateView, CreateView, ListView, DetailView, DeleteView
from django.urls import reverse_lazy
from .models import Chef
from .forms import RegistroChefForm
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ChefSerializer

class RegistroChef(CreateView):
    model = Chef
    form_class = RegistroChefForm
    template_name = "chefs/registrar.html"
    success_url = reverse_lazy('chefs_listar')

class EditarChef(UpdateView):
    model = Chef
    fields = ['tipo_documento', 'nombres', 'apellidos', 'email', 'celular', 'instagram', 'username', 'foto']  # Sin campos de contraseña
    template_name = 'chefs/editar_chef.html'
    success_url = reverse_lazy('chefs_listar')

class ListarChefs(ListView):
    model = Chef
    template_name = "chefs/listar_chefs.html"
    context_object_name = 'chefs'
    paginate_by = 5

class VerChef(DetailView):
    model = Chef
    template_name = "chefs/ver_chef.html"
    context_object_name = 'chef'

class EliminarChef(DeleteView):
    model = Chef
    template_name = "chefs/eliminar_chef.html"
    success_url = reverse_lazy('chefs_listar')

# GET, POST
@api_view(['GET', 'POST'])
def chef_list(request):
    if request.method == 'GET':
        chefs = Chef.objects.all()
        serializer = ChefSerializer(chefs, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ChefSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# GET, PUT, DELETE for a specific Chef
@api_view(['GET', 'PUT', 'DELETE'])
def chef_detail(request, pk):
    try:
        chef = Chef.objects.get(pk=pk)
    except Chef.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ChefSerializer(chef)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = ChefSerializer(chef, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        chef.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)