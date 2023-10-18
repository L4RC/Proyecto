from django.shortcuts import render, redirect

from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.views.generic import CreateView
from django.urls import reverse_lazy
from estudiante.forms import RegistroForm
from django.contrib.auth.views import PasswordChangeView
# Create your views here.

class CustomPasswordChangeView(PasswordChangeView):
    template_name = 'reseteo/cambiar.html'
    success_url = reverse_lazy('cambio')

def cambio_contrasena_exitoso(request):
    return render(request, 'reseteo/cambio.html')



def Estudiante(request):
    return render(request, "Estudiante/estudiante.html")

class RegistroUsuario(CreateView):
    model = User
    template_name ="Estudiante/signupestudiante.html"
    form_class = RegistroForm
    success_url = reverse_lazy('Estudiante')

def cerrar_sesion(request):#sesar sesion.
    logout(request)
    return redirect('Inicio')
