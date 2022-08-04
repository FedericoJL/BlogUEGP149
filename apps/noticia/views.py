from django.shortcuts import render
from .models import Noticia

# Create your views here.

def home(request):
    posts = Noticia.objects.filter(destacada = True)
    return render(request, 'index.html', {'posts':posts})

def noticias(request):
    posts = Noticia.objects.filter(destacada = True)
    return render(request, 'noticias.html', {'posts':posts})

def nosotros(request):
    return render(request, 'nosotros.html')
