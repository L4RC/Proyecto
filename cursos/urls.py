from django.urls import path
from . import views


urlpatterns = [
    path('', views.Asignacion, name="Asignacion"),
    path('Asigna', views.Asigna, name="Asigna"),    
]