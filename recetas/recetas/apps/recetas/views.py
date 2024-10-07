from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from apps.recetas.forms import RecetasForm
from apps.recetas.models import Recetas
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from apps.recetas.serializers import RecetasSerializer

# Vista index
def index(request):
    return render(request, 'recetas/index.html')

# Vista para crear receta
def recetas_view(request):
    if request.method == 'POST':
        form = RecetasForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('recetas_listar')
    else:
        form = RecetasForm()
    return render(request, 'recetas/recetas_form.html', {'form': form})

# Vista para listar recetas
def recetas_list(request):
    recetas = Recetas.objects.all().order_by('id')
    contexto = {'recetas': recetas}
    return render(request, 'recetas/recetas_list.html', contexto)

# Vista para editar receta
def recetas_edit(request, id_recetas):
    receta = Recetas.objects.get(id=id_recetas)
    if request.method == 'GET':
        form = RecetasForm(instance=receta)
    else:
        form = RecetasForm(request.POST, instance=receta)
        if form.is_valid():
            form.save()
        return redirect('recetas_listar')
    return render(request, 'recetas/recetas_form.html', {'form': form})

# Vista para eliminar receta
def recetas_delete(request, id_recetas):
    receta = Recetas.objects.get(id=id_recetas)
    if request.method == 'POST':
        receta.delete()
        return redirect('recetas_listar')
    return render(request, 'recetas/recetas_delete.html', {'receta': receta})

# Clase para listar recetas con paginación
class RecetasList(ListView):
    model = Recetas
    template_name = 'recetas/recetas_list.html'
    paginate_by = 2

# Clase para crear receta
class RecetasCreate(CreateView):
    model = Recetas
    form_class = RecetasForm
    template_name = 'recetas/recetas_form.html'
    success_url = reverse_lazy('recetas_listar')

# Clase para actualizar receta
class RecetasUpdate(UpdateView):
    model = Recetas
    form_class = RecetasForm
    template_name = 'recetas/recetas_form.html'
    success_url = reverse_lazy('recetas_listar')

# Clase para eliminar receta
class RecetasDelete(DeleteView):
    model = Recetas
    template_name = 'recetas/recetas_delete.html'
    success_url = reverse_lazy('recetas_listar')

# Detalle de una receta
def receta_detalle(request, id):
    receta = get_object_or_404(Recetas, id=id)
    return render(request, 'recetas/receta_detalle.html', {'receta': receta})

# API para listar y crear recetas
@api_view(['GET', 'POST'])
def recetas_api_list(request):
    if request.method == 'GET':
        recetas = Recetas.objects.all()
        serializer = RecetasSerializer(recetas, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = RecetasSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# API para ver, actualizar y eliminar una receta específica
@api_view(['GET', 'PUT', 'DELETE'])
def receta_api_detail(request, pk):
    receta = get_object_or_404(Recetas, pk=pk)

    if request.method == 'GET':
        serializer = RecetasSerializer(receta)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = RecetasSerializer(receta, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        receta.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)