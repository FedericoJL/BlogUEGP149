from django.urls import reverse_lazy
from django.shortcuts import render
from .models import Noticia
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView

class BlogListView(ListView):
   model = Noticia
   template_name = 'home.html'


class BlogDetailView(DetailView):
   model = Noticia
   template_name = 'detalles.html'


class AllNews(ListView):
   model = Noticia
   template_name = 'noticias.html'

class AboutUs(ListView):
   model = Noticia
   template_name = 'nosotros.html'

class AddNoticia(CreateView):
    model = Noticia
    fields = ['titulo','resumen', 'texto', 'categoria', 'activo', 'imagen']
    template_name = 'administrar.html'
    success_url = reverse_lazy('blog_list')

class EditarNoticia(UpdateView):
    model = Noticia
    fields = ['titulo','resumen', 'texto', 'categoria', 'activo', 'imagen']
    template_name = 'editar_post.html'
    success_url = reverse_lazy('blog_list')


