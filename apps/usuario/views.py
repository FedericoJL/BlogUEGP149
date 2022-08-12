from django.shortcuts import render
from django.views.generic import CreateView
from .models import Usuario
from .forms import RegistroUsuarioFrom

# Create your views here.

class RegistrarUsuario(CreateView):
	model = Usuario
	form_class = RegistroUsuarioFrom
	template_name = 'usuario/registrar.html'

