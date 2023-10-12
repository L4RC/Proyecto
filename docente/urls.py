from django.urls import path

from . import views
#from django.conf import settings
#from django.conf.urls.static import static 

urlpatterns = [
    path('', views.Profesor, name="Profesor"),    
    path('', views.Iniciar1, name="Iniciar1"),
    path('', views.Registro2, name="Registro2"),
]