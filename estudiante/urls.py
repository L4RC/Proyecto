from django.urls import path

from .views import  cerrar_sesion, logear, Registro
from . import views

urlpatterns = [
#    path('Iniciar', views.Iniciar, name="Iniciar"),    
    path('Estudiante', views.Estudiante, name="Estudiante"),
#    path('Registro', views.Registro, name="Registro"),
    path('Registro', Registro, name='Registro'),

    path('',cerrar_sesion, name="cerrar_sesion"),
    path('logear',logear, name="logear"),    
]