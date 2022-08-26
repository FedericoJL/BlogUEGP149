from msilib.schema import ListView
from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Cursos, Persona, Imagenes
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.

class ListaCursosView(ListView):
    model = Cursos
    context_object_name = 'lista_cursos'
    paginate_by = 1
    template_name = 'curso/cursos.html'
    
    def get_context_data(self, *args, **kwargs):
      cur_menu = Cursos.objects.all()
      context = super(ListaCursosView, self).get_context_data(*args, **kwargs)
      context["cur_menu"] = cur_menu
      return context

class AddCurso(CreateView):
    model = Cursos
    fields = '__all__'
    template_name = 'curso/add_curso.html'
    success_url = reverse_lazy('blog_detail')

    def get_context_data(self, *args, **kwargs):
      cur_menu = Cursos.objects.all()
      context = super(AddCurso, self).get_context_data(*args, **kwargs)
      context["cur_menu"] = cur_menu
      return context
    

class EditarCurso(UpdateView):
    model = Cursos
    fields = '__all__'
    template_name = 'curso/editar_curso.html'
    success_url = reverse_lazy('add_curso')

    def get_context_data(self, *args, **kwargs):
      cur_menu = Cursos.objects.all()
      context = super(EditarCurso, self).get_context_data(*args, **kwargs)
      context["cur_menu"] = cur_menu
      return context


class CursoView(DetailView):
    model = Cursos
    context_object_name = 'curso'
    template_name = 'curso/lista_cursos.html'
    paginate_by = 2

    def get_queryset(self):
        return Cursos.objects.all()

    def get_context_data(self, *args, **kwargs):
      cur_menu = Cursos.objects.all()
      context = super(CursoView, self).get_context_data(*args, **kwargs)
      context["cur_menu"] = cur_menu
      return context


    

