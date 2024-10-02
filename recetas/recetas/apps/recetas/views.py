from django.shortcuts import render, redirect
from django.http import HttpResponse
from apps.recetas.forms import RecetasForm
from apps.recetas.models import Recetas
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404

def index(request):
    return render(request, 'recetas/index.html')


def recetas_view(request):
    if request.method =='POST':
        form = RecetasForm(request.POST)

        if form.is_valid():
            form.save()
        return redirect('recetas_listar')
    else:
        form = RecetasForm()
    return render(request, 'recetas/recetas_form.html', {'form':form})

def recetas_list(request):
    recetas = Recetas.objects.all().order_by('id')
    contexto = {'recetas':recetas}
    return render(request, 'recetas/recetas_list.html', contexto)


def recetas_edit(request, id_recetas):
    recetas = Recetas.objects.get(id=id_recetas)
    if request.method == 'GET':
        form = RecetasForm(instance=recetas)
    else:
        form = RecetasForm(request.POST, instance=recetas)
        if form.is_valid():
            form.save()
        return redirect('recetas_listar')
    return render(request, 'recetas/recetas_form.html', {'form':form})

def recetas_delete(request, id_recetas):
    recetas = Recetas.objects.get(id=id_recetas)
    if request.method =='POST':
        recetas.delete()
        return redirect('recetas_listar')
    return render(request, 'recetas/recetas_delete.html', {'recetas':recetas})

class RecetasList(ListView):
    model = Recetas
    template_name = 'recetas/recetas_list.html'
    paginate_by = 2

class RecetasCreate(CreateView):
    model = Recetas
    form_class = RecetasForm
    template_name = 'recetas/recetas_form.html'
    success_url = reverse_lazy('recetas_listar')

class RecetasUpdate(UpdateView):
    model = Recetas
    form_class = RecetasForm
    template_name = 'recetas/recetas_form.html'
    success_url = reverse_lazy('recetas_listar')

class RecetasDelete(DeleteView):
    model = Recetas
    template_name = 'recetas/recetas_delete.html'
    success_url = reverse_lazy('recetas_listar')

def receta_detalle(request, id):
    receta = get_object_or_404(Recetas, id=id)
    return render(request, 'recetas/receta_detalle.html', {'receta': receta})