from django.urls import path
from estudiante.views import RegistroUsuario
from django.contrib.auth.views import LoginView

from .views import cerrar_sesion, CustomPasswordChangeView, cambio_contrasena_exitoso
from . import views


urlpatterns = [
    path('Estudiante', views.Estudiante, name="Estudiante"),#pagina de estudiante
    path('Registro', RegistroUsuario.as_view(), name="Registro"),#para registrar usuario 
    path('',cerrar_sesion, name="cerrar_sesion"),#para cerrar sesion
    path('Iniciar', LoginView.as_view(template_name='estudiante/signinestudiante.html'), name='Iniciar'),#para iniciar sesion
    path('cambiar', CustomPasswordChangeView.as_view(), name='cambiar'),
    path('cambio', cambio_contrasena_exitoso, name='cambio'),
]