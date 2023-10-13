from django.shortcuts import render

# Create your views here.

def Estudiante1(request):
    return render(request, "Estudiante/estudiante.html")

def Iniciar(request):
    return render(request, "Estudiante/signinestudiante.html")

def Registro(request):
    return render(request, "Estudiante/signupestudiante.html")