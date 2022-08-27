from django.urls import path
from .views import AddCurso, EditarCurso, EliminarCurso, ListaCursosView, CursoView, AddPersona, export_inscriptos_xls



urlpatterns = [

      path('export/xls/', export_inscriptos_xls, name='export_xls'),
      path('add_persona/', AddPersona.as_view(), name='add_persona'),
      path('borrar/<int:pk>', EliminarCurso.as_view(), name='borrar_curso'),
      path('editar/<int:pk>', EditarCurso.as_view(), name='editar_curso'),
      path('curso/<int:pk>', CursoView.as_view(), name='curso'),
      path('add_curso/', AddCurso.as_view(), name='add_curso'),
      path('', ListaCursosView.as_view(), name='lista_cursos'),
      
]