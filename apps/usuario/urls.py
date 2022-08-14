from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import RegistrarUsuario, ModificarUsuario, DeleteUsuario


urlpatterns = [
    path('', RegistrarUsuario.as_view(), name="addUsuario"),
    path('modificarUsuario/<int:pk>', ModificarUsuario.as_view(), name="modificarUsuario"),
    path('eliminarUsuario/<int:pk>', DeleteUsuario.as_view(), name="eliminarUsuario"),
    path('login/', LoginView.as_view(template_name="usuario/login.html"),name="login"),
    path('logout/', LogoutView.as_view(),name="logout"),

  
]