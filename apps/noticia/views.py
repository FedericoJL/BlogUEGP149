from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'index.html')

def noticias(request):
    return render(request, 'noticias.html')

def nosotros(request):
    return render(request, 'nosotros.html')
