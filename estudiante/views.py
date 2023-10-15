from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages

# Create your views here.

def Estudiante(request):
    return render(request, "Estudiante/estudiante.html")

def Iniciar(request):
    return render(request, "Estudiante/signinestudiante.html")

#def Registro(request):
#    return render(request, "Estudiante/signupestudiante.html")

class VRegistro(View): #para el registro 
    def get(self, request):
        form = UserCreationForm()
        return render(request, "Estudiante/signupestudiante.html", {"form":form})
    
    def post(self, request):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
#            return redirect('estudiante')
            return render(request, "Estudiante/estudiante.html")


        else: 
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])
        return render(request, "Estudiante/signupestudiante.html", {"form":form})

def cerrar_sesion(request):#sesar sesion.
    logout(request)
    return redirect('Inicio')

def logear(request):
    form = AuthenticationForm()
    return render(request, "Estudiante/signinestudiante.html",{"form":form})
