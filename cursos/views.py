from django.shortcuts import render, redirect, get_object_or_404

from .models import Curso
from django.db import models
from django.db.models import Count
from django.contrib.auth.models import User
from .models import Curso
from estudiante.forms import CustomUserCreationForm  # Asegúrate de importar tu formulario


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

"""def inscribirse_curso(request, curso_id):
    # Verificar si el usuario actual existe en la tabla auth_user
    try:
        user = User.objects.get(username=request.user.username)
        # Resto de la lógica para la inscripción en el curso
        # Asegúrate de que tengas un formulario de inscripción adecuado y procesa los datos del formulario
        if request.method == 'POST':
            formulario = CustomUserCreationForm(request.POST)
            if formulario.is_valid():
                # Procesa los datos del formulario y realiza la inscripción al curso
                # Asume que el formulario tiene un campo para el curso y los datos del estudiante
                curso = Curso.objects.get(id=curso_id)
                estudiante = user  # Usar el usuario autenticado
                if estudiante not in curso.estudiantes_inscritos.all():
                    curso.estudiantes_inscritos.add(estudiante)
                    return redirect('lista_cursos')
                else:
                    # El estudiante ya está inscrito en el curso, maneja esto como desees
                    return redirect('lista_cursos')
        else:
            # Si no se recibió un POST request, puedes renderizar el formulario de inscripción
            formulario = CustomUserCreationForm()

        # Resto de la lógica para renderizar el formulario

    except User.DoesNotExist:
        # Manejar el caso en el que el usuario no existe en la tabla auth_user
        pass
"""
def inscribirse_curso(request, curso_id):
    try:
        # Verificar si el usuario actual existe en la tabla auth_user
        user = User.objects.get(username=request.user.username)

        # Obtener el curso
        curso = get_object_or_404(Curso, id=curso_id)

        if request.method == 'POST':
            # Si se envió un formulario POST, procesar los datos del formulario
            formulario = CustomUserCreationForm(request.POST)

            if formulario.is_valid():
                # El formulario es válido, continuar con la inscripción
                estudiante = user
                if estudiante not in curso.estudiantes_inscritos.all():
                    curso.estudiantes_inscritos.add(estudiante)
                    return redirect('lista_cursos')
                else:
                    # El estudiante ya está inscrito en el curso, maneja esto como desees
                    return redirect('lista_cursos')
        else:
            # Si no se recibió un POST request, renderizar el formulario de inscripción
            formulario = CustomUserCreationForm()

        # Renderizar el formulario y cualquier otro contenido adicional
        return render(request, 'cursos/inscripcion_form.html', {'formulario': formulario, 'curso': curso})
    except User.DoesNotExist:
        # Manejar el caso en el que el usuario no existe en la tabla auth_user
        # Puedes redirigir al usuario a una página de error o mostrar un mensaje de error
        return redirect('pagina_de_error')
    
def cursos_asignados(request):
    # Obtén el usuario actual
    usuario = request.user
    # Consulta los cursos asignados al usuario
    cursos_asignados = Curso.objects.filter(estudiantes_inscritos=usuario)
    return render(request, 'cursos/cursos_asignados.html', {'cursos_asignados': cursos_asignados})    