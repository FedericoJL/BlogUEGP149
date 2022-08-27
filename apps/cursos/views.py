from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Cursos, Persona
from apps.noticia.models import Categoria
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
import xlwt
from django.http import HttpResponse

# Create your views here.

class ListaCursosView(ListView):
    model = Cursos
    context_object_name = 'lista_cursos'
    paginate_by = 1
    template_name = 'curso/cursos.html'
    
    def get_context_data(self, *args, **kwargs):
        cur_menu = Cursos.objects.all()
        cat_menu = Categoria.objects.all()
        context = super(ListaCursosView, self).get_context_data(*args, **kwargs)
        context["cur_menu"] = cur_menu
        context["cat_menu"] = cat_menu
        return context

class AddCurso(CreateView):
    model = Cursos
    fields = '__all__'
    template_name = 'curso/add_curso.html'
    success_url = reverse_lazy('postear')

    def get_context_data(self, *args, **kwargs):
        cur_menu = Cursos.objects.all()
        cat_menu = Categoria.objects.all()
        context = super(AddCurso, self).get_context_data(*args, **kwargs)
        context["cur_menu"] = cur_menu
        context["cat_menu"] = cat_menu
        return context
    

class EditarCurso(UpdateView):
    model = Cursos
    fields = '__all__'
    template_name = 'curso/editar_curso.html'
    success_url = reverse_lazy('postear')

    def get_context_data(self, *args, **kwargs):
        cur_menu = Cursos.objects.all()
        cat_menu = Categoria.objects.all()
        context = super(EditarCurso, self).get_context_data(*args, **kwargs)
        context["cur_menu"] = cur_menu
        context["cat_menu"] = cat_menu
        return context

class EliminarCurso(DeleteView):
    model = Cursos
    template_name = "curso/borrar_curso.html"
    success_url = reverse_lazy('postear')

    def get_context_data(self, *args, **kwargs):
        cur_menu = Cursos.objects.all()
        cat_menu = Categoria.objects.all()
        context = super(EliminarCurso, self).get_context_data(*args, **kwargs)
        context["cur_menu"] = cur_menu
        context["cat_menu"] = cat_menu
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
        cat_menu = Categoria.objects.all()
        context = super(CursoView, self).get_context_data(*args, **kwargs)
        context["cur_menu"] = cur_menu
        context["cat_menu"] = cat_menu
        return context
   
class AddPersona(CreateView):
    model = Persona
    fields = '__all__'
    template_name = 'curso/add_persona.html'
    success_url = reverse_lazy('last_x_posts')

    def get_context_data(self, *args, **kwargs):
        cur_menu = Cursos.objects.all()
        cat_menu = Categoria.objects.all()
        context = super(AddPersona, self).get_context_data(*args, **kwargs)
        context["cur_menu"] = cur_menu
        context["cat_menu"] = cat_menu
        return context


def export_inscriptos_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="inscriptos.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Persona')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Nombre', 
    'Apellidos', 
    'DNI', 
    'CUIL', 
    'Provincia', 
    'Ciudad', 
    'Dirección', 
    'Email',
    'Curso', 
    ]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = Persona.objects.all().values_list(
        'nombre', 
        'apellidos', 
        'dni', 
        'cuil',
        'provincia', 
        'ciudad', 
        'direccion', 
        'email',
        'curso__nombre'
        )
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response



    