from django.urls import path
from . import views

app_name = "carro"

urlpatterns = [
    path("agregar/<int:Curso_id>/", views.agregar_curso, name="agregar"),
    path("eliminar/<int:Curso_id>/", views.eliminar_curso, name="eliminar"),
#    path("limpiar/<int:Curso_id>/", views.limpiar_curso, name="limpiar"),
]