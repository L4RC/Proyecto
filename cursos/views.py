from django.shortcuts import render, redirect
from .models import Curso
from django.db import models
from django.db.models import Count
from estudiante.models import CustomUser


# Create your views here.
def Asignacion(request):#Tabla de cursos que se muestra en pagina principal
    cursos = Curso.objects.all()
    return render(request, "courses/table.html", {"cursos":cursos})

def Asigna(request):#tabla de cursos dentro del usuario
    cursos = Curso.objects.all()
    return render(request,"courses/asignado.html", {"cursos":cursos})


def desasigna(request):#tabla de cursos dentro del usuario
    cursos = Curso.objects.all()
    return render(request,"courses/desasignar.html", {"cursos":cursos})


def lista_cursos(request):
    cursos_disponibles = Curso.objects.annotate(num_inscritos=Count('estudiantes_inscritos')).filter(cupo__gt=models.F('num_inscritos'))

#    cursos_disponibles = Curso.objects.filter(cupo__gt = models.Count('estudiantes_inscritos'))
    return render(request, 'cursos/lista_cursos.html', {'cursos': cursos_disponibles})

def inscribirse_curso(request, curso_id):
    curso = Curso.objects.get(id=curso_id)
    estudiante = CustomUser.objects.get(username=request.user.username)

    if estudiante not in curso.estudiantes_inscritos.all():
        curso.estudiantes_inscritos.add(estudiante)
        return redirect('lista_cursos')
    else:
        return redirect('lista_cursos')


