from django.urls import path

from . import views
#from django.conf import settings
#from django.conf.urls.static import static 

urlpatterns = [
    path('Profesor', views.Profesor, name="Profesor"),    
    path('Iniciar1', views.Iniciar1, name="Iniciar1"),
    path('Registro2', views.Registro2, name="Registro2"),
]