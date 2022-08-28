from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import EditarIntegrante, RegistrarUsuario, ModificarUsuario, DeleteUsuario


urlpatterns = [
    
    path('', RegistrarUsuario.as_view(), name="addUsuario"),
    path('modificarUsuario/<int:pk>', ModificarUsuario.as_view(), name="modificarUsuario"),
    path('eliminarUsuario/<int:pk>', DeleteUsuario.as_view(), name="eliminarUsuario"),
    path('editar_integrante/<int:pk>', EditarIntegrante.as_view(), name="editar_integrante"),
    path('login/', LoginView.as_view(template_name="usuario/login.html"),name="login"),
    path('logout/', LogoutView.as_view(),name="logout"),

  
]