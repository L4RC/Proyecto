from django.shortcuts import render
from .asignar import Asignar

from .models import Seleccion
from django.shortcuts import redirect 

# Create your views here.

def agregar_seleccion(request, seleleccion_id):

    asignar = Asignar(request)
    seleccion = Seleccion.objects.get(id=seleleccion_id)
    asignar.agregar(seleccion=seleccion)
    return redirect(" ")

def eliminar_seleccion(request, seleleccion_id):

    asignar = Asignar(request)
    seleccion = Seleccion.objects.get(id=seleleccion_id)
    asignar.eliminar(seleccion=seleccion)
    return redirect(" ") #redireccionarl al html

def restar_seleccion(request, seleleccion_id):

    asignar = Asignar(request)
    seleccion = Seleccion.objects.get(id=seleleccion_id)
    asignar.restar_seleccion(seleccion=seleccion)
    return redirect(" ")

def limpiar_asignar(request, seleleccion_id):

    asignar = Asignar(request)
    asignar.limpiar_asignar()
    return redirect(" ")

