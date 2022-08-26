
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404
from apps.noticia.forms import PostForm
from .models import Noticia, Categoria
from apps.cursos.models import Cursos
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


class BlogListView(TemplateView):
   model = Noticia
   template_name = 'home.html'
   def get_context_data(self, *args, **kwargs):
      last_six_posts = Noticia.objects.filter(activo=True).order_by('-fecha')[1:5]
      last_post = Noticia.objects.filter(activo=True).order_by('-fecha')[:1]
      cat_menu = Categoria.objects.all()
      cur_menu = Cursos.objects.all()
      return {'last_x_posts': last_six_posts, 'last_post': last_post, 'cat_menu': cat_menu, 'cur_menu': cur_menu}
   

class BlogDetailView(DetailView):
   model = Noticia
   template_name = 'noticia/detalles.html'

   def get_context_data(self, *args, **kwargs):
      cat_menu = Categoria.objects.all()
      context = super(BlogDetailView, self).get_context_data(*args, **kwargs)
      context["cat_menu"] = cat_menu
      return context
   

class AllNews(ListView):
   model = Noticia
   context_object_name = 'all_posts'
   paginate_by = 2
   template_name = 'noticia/noticias.html'

   def get_queryset(self):
    return Noticia.objects.all().order_by('-fecha')
   
   def get_context_data(self, *args, **kwargs):
      cat_menu = Categoria.objects.all()
      context = super(AllNews, self).get_context_data(*args, **kwargs)
      context["cat_menu"] = cat_menu
      return context

   
class AboutUs(ListView):
   model = Noticia
   template_name = 'nosotros.html'
   
   def get_context_data(self, *args, **kwargs):
        cat_menu = Categoria.objects.all()
        context = super(AboutUs, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

   
class AddNoticia(CreateView):
   model = Noticia
   form_class = PostForm
   #fields = ['titulo','resumen', 'texto', 'categoria', 'activo', 'imagen']
   template_name = 'noticia/administrar.html'
   success_url = reverse_lazy('last_x_posts')

   def get_context_data(self, *args, **kwargs):
      cat_menu = Categoria.objects.all()
      context = super(AddNoticia, self).get_context_data(*args, **kwargs)
      context["cat_menu"] = cat_menu
      return context
   

class EditarNoticia(UpdateView):
   model = Noticia
   fields = ['titulo','resumen', 'texto', 'categoria', 'activo', 'imagen']
   template_name = 'noticia/editar_post.html'
   success_url = reverse_lazy('last_x_posts')

   def get_context_data(self, *args, **kwargs):
      cat_menu = Categoria.objects.all()
      context = super(EditarNoticia, self).get_context_data(*args, **kwargs)
      context["cat_menu"] = cat_menu
      return context


class AddCategory(CreateView):
   model = Categoria
   fields = ['nombre', 'activo']
   template_name = 'noticia/add_category.html'
   success_url = reverse_lazy('postear')

   def get_context_data(self, *args, **kwargs):
      cat_menu = Categoria.objects.all()
      context = super(AddCategory, self).get_context_data(*args, **kwargs)
      context["cat_menu"] = cat_menu
      return context


class UpdateCategory(UpdateView):
   model = Categoria
   fields = ['nombre', 'activo']
   template_name = 'noticia/edit_category.html'
   success_url = reverse_lazy('postear')

   def get_context_data(self, *args, **kwargs):
      cat_menu = Categoria.objects.all()
      context = super(UpdateCategory, self).get_context_data(*args, **kwargs)
      context["cat_menu"] = cat_menu
      return context


 
class CategoryPost(ListView):
   model = Noticia
   context_object_name = 'category_posts'
   template_name = 'noticia/categories.html'
   paginate_by = 2

   def get_queryset(self):
      self.category = get_object_or_404(Categoria, pk=self.kwargs['pk'] )
      return Noticia.objects.filter(categoria=self.category)
   
   def get_context_data(self, *args, **kwargs):
      context = super(CategoryPost, self).get_context_data(**kwargs)
      context['category'] = self.category
      return context

   def get_context_data(self, *args, **kwargs):
      cat_menu = Categoria.objects.all()
      context = super(CategoryPost, self).get_context_data(*args, **kwargs)
      context["cat_menu"] = cat_menu
      return context

   

