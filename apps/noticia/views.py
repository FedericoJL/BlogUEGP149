from django.shortcuts import render
from .models import Noticia

# Create your views here.

def home(request):
    noticias = Noticia.objects.filter(activo = True)
    return render(request, 'index.html', {'noticias':noticias})

def noticias(request):
    return render(request, 'noticias.html')

def nosotros(request):
    return render(request, 'nosotros.html')
