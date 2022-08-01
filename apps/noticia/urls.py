from django.urls import path
from .views import home, noticias, nosotros

urlpatterns = [
    path('', home, name = 'index'),
    path('noticias/', noticias, name = 'noticias'),
    path('nosotros/', nosotros, name = 'nosotros'),

]