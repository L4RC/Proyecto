from django.shortcuts import render, redirect
#from django.views.generic import View
from django.contrib.auth import login, logout
from django.contrib.auth.forms import  AuthenticationForm, authenticate
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
            password = form.cleaned_data['password']
            password2 = form.cleaned_data['password2']
            
            if password == password2:
                user = form.save()
                login(request, user)  # Inicia sesión al usuario después del registro
                return render(request, 'Estudiante/estudiante.html')

            else:
                messages.error(request, 'Las contraseñas no coinciden.')
        else:
            messages.error(request, 'Hubo un problema con el formulario de registro.')

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
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            username = authenticate(username = username, password = password)
            if username is not None:
                login(request, username)
            #    return redirect('estudiante')
                return render(request, "Estudiante/estudiante.html")
            
            else:
                messages.error(request, "Usuario no válido")

        else:
            messages.error(request, "Información incorrecta")

    form = AuthenticationForm()
    return render(request, "Estudiante/signinestudiante.html",{"form":form})

"""
def logear(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return render(request, 'Estudiante/estudiante.html')

#            return redirect('Registro')
    else:
        form = AuthenticationForm()
    return render(request, 'Estudiante/signinestudiante.html', {'form': form})
"""
