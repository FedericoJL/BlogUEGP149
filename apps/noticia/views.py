from django.shortcuts import render
from .models import Noticia

# Create your views here.

def home(request):
    return render(request, 'index.html')

def noticias(request):
    return render(request, 'noticias.html')

def nosotros(request):
    return render(request, 'nosotros.html')
