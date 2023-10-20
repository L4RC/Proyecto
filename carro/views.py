from django.shortcuts import render, redirect

from .carro import Carro
from cursos.models import Curso

# Create your views here.

def agregar_curso(request, Curso_id):
    carro = Carro(request)
    curso = Curso.objects.get(id=Curso_id)
    carro.agregar(Curso=curso)
    return redirect("Asigna")

def eliminar_curso(request, Curso_id):
    carro = Carro(request)
    curso = Curso.objects.get(id=Curso_id)
    carro.eliminar(Curso=curso)
    return redirect("desasigna")

#def limpiar_curso(request, curso_id):
#    carro = Carro(request)
#    carro.limpiar()
#    return redirect("Asigna")
