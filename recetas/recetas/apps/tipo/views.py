from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView
from apps.tipo.models import Descripcion, Receta
from apps.tipo.forms import DescripcionForm, RecetaForm
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import DescripcionSerializer, RecetaSerializer

def index_tipo(request):
    return HttpResponse("Soy la pagina principal de la app tipo")

class TipoList(ListView):
    model = Receta
    template_name = 'tipo/tipo_list.html'
    context_object_name = 'recetas' 

class TipoCreate(CreateView):
    model = Receta
    template_name = 'tipo/tipo_form.html'
    form_class = RecetaForm
    second_form_class = DescripcionForm
    success_url = reverse_lazy('tipo_listar')

    def get_context_data(self, **kwargs):
        context = super(TipoCreate, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.get_form_class()()
        if 'form2' not in context:
            context['form2'] = self.second_form_class()
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        form2 = self.second_form_class(request.POST)
        
        if form.is_valid() and form2.is_valid():
            descripcion = form2.save() 
            receta = form.save(commit=False) 
            receta.descripcion = descripcion 
            receta.save()  
            return HttpResponseRedirect(self.success_url)
        return self.render_to_response(self.get_context_data(form=form, form2=form2))


class TipoUpdate(UpdateView):
    model = Receta
    second_model = Descripcion
    template_name = 'tipo/tipo_form.html'
    form_class = RecetaForm
    second_form_class = DescripcionForm
    success_url = reverse_lazy('tipo_listar')

    def get_context_data(self, **kwargs):
        context = super(TipoUpdate, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk', 0)
        plato = self.model.objects.get(id=pk)
        descripcion = self.second_model.objects.get(id=plato.descripcion_id)
        if 'form' not in context:
            context['form'] = self.form_class()
        if 'form2' not in context:
            context['form2'] = self.second_form_class(instance=descripcion)
        context['id'] = pk
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        id_plato = kwargs['pk']
        plato = self.model.objects.get(id=id_plato)
        descripcion = self.second_model.objects.get(id=plato.descripcion_id)
        form = self.form_class(request.POST, instance=plato)
        form2 = self.second_form_class(request.POST, instance=descripcion)
        if form.is_valid and form2.is_valid():
            form.save()
            form2.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return HttpResponseRedirect(self.get_success_url())

class TipoDelete(DeleteView):
    model = Receta
    template_name = 'tipo/tipo_delete.html'
    success_url = reverse_lazy('tipo_listar')

class TipoDetail(DetailView):
    model = Receta
    template_name = 'tipo/tipo_detalle.html'
    
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Descripcion, Receta
from .serializers import DescripcionSerializer, RecetaSerializer

# Vistas para Descripcion

@api_view(['GET', 'POST'])
def descripcion_list(request):
    if request.method == 'GET':
        descripciones = Descripcion.objects.all()
        serializer = DescripcionSerializer(descripciones, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = DescripcionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def descripcion_detail(request, pk):
    try:
        descripcion = Descripcion.objects.get(pk=pk)
    except Descripcion.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DescripcionSerializer(descripcion)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = DescripcionSerializer(descripcion, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        descripcion.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def descripcion_list(request):
    if request.method == 'GET':
        descripciones = Descripcion.objects.all()
        serializer = DescripcionSerializer(descripciones, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = DescripcionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def descripcion_detail(request, pk):
    try:
        descripcion = Descripcion.objects.get(pk=pk)
    except Descripcion.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DescripcionSerializer(descripcion)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = DescripcionSerializer(descripcion, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        descripcion.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Vistas para Receta

@api_view(['GET', 'POST'])
def receta_list(request):
    if request.method == 'GET':
        recetas = Receta.objects.all()
        serializer = RecetaSerializer(recetas, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = RecetaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def receta_detail(request, pk):
    try:
        receta = Receta.objects.get(pk=pk)
    except Receta.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = RecetaSerializer(receta)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = RecetaSerializer(receta, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        receta.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)