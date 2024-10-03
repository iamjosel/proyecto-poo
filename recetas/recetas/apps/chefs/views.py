from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from .models import Chef
from .forms import RegistroChefForm

class RegistroChef(CreateView):
    model = Chef
    form_class = RegistroChefForm
    template_name = "chefs/registrar.html"
    success_url = reverse_lazy('chefs_listar')

class ListarChefs(ListView):
    model = Chef
    template_name = "chefs/listar_chefs.html"
    context_object_name = 'chefs'