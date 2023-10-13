from django.urls import path

from . import views


urlpatterns = [
    path('', views.Iniciar, name="Iniciar"),    
    path('', views.Estudiante1, name="Estudiante1"),
    path('', views.Registro, name="Registro"),
]