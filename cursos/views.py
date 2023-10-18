from django.shortcuts import render
from cursos.models import Curso
# Create your views here.
def Asignacion(request):#Tabla de cursos que se muestra en pagina principal
    cursos = Curso.objects.all()
    return render(request, "courses/table.html", {"cursos":cursos})

def Asigna(request):#tabla de cursos dentro del usuario
    cursos = Curso.objects.all()
    return render(request,"courses/asignado.html", {"cursos":cursos})


#def Asigna(request):#tabla de cursos dentro del usuario
#    cursos = Curso.objects.all()
#    return render(request,"courses/asignado.html", {"cursos":cursos})

