from django.shortcuts import render, redirect
from django.contrib.auth import logout, login
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from .forms import CustomUserCreationForm
from estudiante.forms import CustomUserCreationForm
from .utils import send_registration_email 
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
# Create your views here.

def user_profile(request, username):
    # Obtén el usuario o muestra una página 404 si no existe
    user = get_object_or_404(User, username=username)
    # Puedes personalizar esta vista para mostrar los datos del perfil del usuario
    return render(request, 'Estudiante/user_profile.html', {'user': user})


############
class CustomPasswordChangeView(PasswordChangeView):
    template_name = 'reseteo/cambiar.html'
    success_url = reverse_lazy('cambio')

def cambio_contrasena_exitoso(request):
    return render(request, 'reseteo/cambio.html')



def Estudiante(request):
    return render(request, "Estudiante/estudiante.html")

def cerrar_sesion(request):#sesar sesion.
    logout(request)
    return redirect('Inicio')

def signup(request):#registrar usuario
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            grupo_estudiantes, created = Group.objects.get_or_create(name='Estudiantes')
            user.groups.add(grupo_estudiantes)                        
            send_registration_email(user.email)  # Llama a la función para enviar el correo            
            login(request, user)  # Inicia sesión automáticamente después del registro
            return redirect('Estudiante')  # Redirige a la página principal
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

