from django.shortcuts import render

# Create your views here.

def Profesor(request):
    return render(request, "Docente/profesor.html")

def Iniciar1(request):
    return render(request, "Docente/signindocente.html")

def Registro2(request):
    return render(request, "Docente/signupdocente.html")