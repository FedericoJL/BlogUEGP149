from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import Integrantes, Usuario
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
	template_name = 'usuario/eliminar_usuario.html'
	success_url = reverse_lazy('last_x_posts')


class EditarIntegrante(UpdateView):
	model = Integrantes
	fields = "__all__"
	template_name = 'usuario/editar_integrante.html'
	success_url = reverse_lazy('postear')