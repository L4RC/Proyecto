from django.urls import path

from .views import VRegistro, cerrar_sesion, logear
from . import views

urlpatterns = [
    path('Iniciar', views.Iniciar, name="Iniciar"),    
    path('Estudiante', views.Estudiante, name="Estudiante"),
#    path('Registro', views.Registro, name="Registro"),
    path('Registro', VRegistro.as_view(), name="Registro"),
    path('',cerrar_sesion, name="cerrar_sesion"),
    path('loger',logear, name="logear"),    

]