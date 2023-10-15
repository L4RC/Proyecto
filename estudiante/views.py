from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import  AuthenticationForm
from django.contrib import messages
from .forms import RegistrationForm  # Importa el formulario desde forms.py

# Create your views here.

def Estudiante(request):
    return render(request, "Estudiante/estudiante.html")

#def Iniciar(request):
#    return render(request, "Estudiante/signinestudiante.html")

#def Registro(request):
#    return render(request, "Estudiante/signupestudiante.html")
"""
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

"""
def Registro(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Inicia sesión al usuario después del registro
            return redirect('estudiante')  # Redirige a la página de inicio o a donde desees
    else:
        form = RegistrationForm()
    
    return render(request, 'Estudiante/signupestudiante.html', {'form': form})



def cerrar_sesion(request):#sesar sesion.
    logout(request)
    return redirect('Inicio')

def logear(request): #para iniciar sesion estudiante
    if request.method =="POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            nombre_usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")
            usuario = authenticate(username = nombre_usuario, password = contra)
            if usuario is not None:
                login(request, usuario)
            #    return redirect('estudiante')
                return render(request, "Estudiante/estudiante.html")
            
            else:
                messages.error(request, "Usuario no válido")

        else:
            messages.error(request, "Información incorrecta")

    form = AuthenticationForm()
    return render(request, "Estudiante/signinestudiante.html",{"form":form})


