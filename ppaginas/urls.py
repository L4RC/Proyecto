from django.urls import path
from ppaginas import views #importa las views de la carpeta ppgainas

urlpatterns = [
    path('', views.Inicio, name="Inicio"),
    path('Administrador', views.Administrador, name="Administrador"),
    path('index', views.index, name="index"),    
    path('Escuelas', views.Escuelas, name="Escuelas"),
    path('Error', views.Error, name="Error"),    
]