from django.urls import path
from . import views


urlpatterns = [
    path('', views.Asignacion, name="Asignacion"),
    path('Asigna', views.Asigna, name="Asigna"),   
    path('desasigna', views.desasigna, name="desasigna"),  
    path('inscribir_curso/<int:curso_id>/', views.inscribirse_curso, name='inscribirse_curso'),
    path('curso/', views.lista_cursos, name="lista_cursos"),
    path('cursos-asignados/', views.cursos_asignados, name='cursos_asignados')

]

