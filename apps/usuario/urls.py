from django.urls import path
from .views import RegistrarUsuario

#from .views import

urlpatterns = [
    path('', RegistrarUsuario.as_view() ,name="addUsuario"),
  
]