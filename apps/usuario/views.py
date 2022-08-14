from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import Usuario
from .forms import RegistroUsuarioFrom

# Create your views here.

class RegistrarUsuario(CreateView):
	model = Usuario
	form_class = RegistroUsuarioFrom
	template_name = 'usuario/registrar.html'
	success_url = reverse_lazy('login')

class ModificarUsuario(UpdateView):
	model = Usuario
	form_class = RegistroUsuarioFrom
	template_name = 'usuario/modificar.html'
	success_url = reverse_lazy('login')

class DeleteUsuario(DeleteView):
	model = Usuario
	success_url = reverse_lazy('blog_list')

