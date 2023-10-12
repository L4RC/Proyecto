from django.shortcuts import render

# Create your views here.

def Student(request):
    return render(request, "Estudiante/estudiante.html")

def Iniciar(request):
    return render(request, "Estudiante/signinestudiante.html")

def Registro(request):
    return render(request, "Estudiante/signupestudiante.html")