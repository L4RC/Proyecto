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
    return render(request, 'resetep/cambio.html')



def Estudiante(request):
    return render(request, "Estudiante/estudiante.html")

class RegistroUsuario(CreateView):
    model = User
    template_name ="Estudiante/signupestudiante.html"
    form_class = RegistroForm
    success_url = reverse_lazy('Estudiante')

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
            return redirect('Estudiante')

        else: 
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])
        return render(request, "Estudiante/signupestudiante.html", {"form":form})

def logear(request):#Para iniciar sesion, validando usuario y contraseña
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('Estudiante')  # Reemplaza 'página_principal' con la URL a la que deseas redirigir al usuario después del inicio de sesión
            else:
                error_message = "Nombre de usuario o contraseña incorrectos."
                return render(request, 'Estudiante/signinestudiante.html', {'form': form, 'error_message': error_message})
    else:
        form = AuthenticationForm()
    return render(request, 'Estudiante/signinestudiante.html', {'form': form})
""" 
def cerrar_sesion(request):#sesar sesion.
    logout(request)
    return redirect('Inicio')
