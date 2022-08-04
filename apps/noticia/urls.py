from django.urls import path
from .views import home, noticias, nosotros

urlpatterns = [
    path('', home, name = 'index'),
    path('noticia/', noticias, name = 'noticia'),
    path('nosotros/', nosotros, name = 'nosotros'),
]
