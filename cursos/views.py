from django.shortcuts import render
from cursos.models import Curso


# Create your views here.
def Asignacion(request):#cursos

    cursos = Curso.objects.all()
    return render(request, "courses/table.html", {"cursos":cursos})
