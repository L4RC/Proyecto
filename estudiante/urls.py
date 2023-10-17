from django.urls import path
from estudiante.views import RegistroUsuario
from django.contrib.auth.views import LoginView

from .views import cerrar_sesion, CustomPasswordChangeView, cambio_contrasena_exitoso
from . import views


urlpatterns = [
    path('Estudiante', views.Estudiante, name="Estudiante"),
    path('Registro', RegistroUsuario.as_view(), name="Registro"),
    path('',cerrar_sesion, name="cerrar_sesion"),
    path('Iniciar', LoginView.as_view(template_name='estudiante/signinestudiante.html'), name='Iniciar'),
#    path('cambiar_contrasena/', PasswordChangeView.as_view(template_name='cambiar_contrasena.html', success_url='cambio-contrasena-exitoso/'), name='cambiar_contrasena'),
    # Otras URL de tu aplicación
    path('cambiar', CustomPasswordChangeView.as_view(), name='cambiar'),
    path('cambio', cambio_contrasena_exitoso, name='cambio'),



]