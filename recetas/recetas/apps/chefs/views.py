from django.views.generic import UpdateView, CreateView, ListView, DetailView, DeleteView
from django.urls import reverse_lazy
from .models import Chef
from .forms import RegistroChefForm

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

class VerChef(DetailView):
    model = Chef
    template_name = "chefs/ver_chef.html"
    context_object_name = 'chef'

class EliminarChef(DeleteView):
    model = Chef
    template_name = "chefs/eliminar_chef.html"
    success_url = reverse_lazy('chefs_listar')