from django.urls import path
from .views import AddCurso, EditarCurso, ListaCursosView, CursoView



urlpatterns = [

      path('editar/<int:pk>', EditarCurso.as_view(), name='editar_curso'),
      path('curso/<int:pk>', CursoView.as_view(), name='curso'),
      path('add_curso/', AddCurso.as_view(), name='add_curso'),
      path('', ListaCursosView.as_view(), name='lista_cursos'),
      
]