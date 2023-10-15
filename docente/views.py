from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages

# Create your views here.

def Profesor(request):
    return render(request, "Docente/profesor.html")

#def Iniciar1(request):
#    return render(request, "Docente/signindocente.html")

def Registro2(request):
    return render(request, "Docente/signupdocente.html")

def cerrar_sesion(request):#sesar sesion.
    logout(request)
    return redirect('Inicio')

def logear2(request): #para iniciar sesion profesor
    if request.method =="POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            nombre_usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")
            usuario = authenticate(username = nombre_usuario, password = contra)
            if usuario is not None:
                login(request, usuario)
            #    return redirect('estudiante')
                return render(request, "Docente/profesor.html")
            
            else:
                messages.error(request, "Usuario no válido")

        else:
            messages.error(request, "Información incorrecta")

    form = AuthenticationForm()
    return render(request, "Docente/signindocente.html",{"form":form})
