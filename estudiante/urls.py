from django.urls import path
#from estudiante.views import RegistroUsuario
from django.contrib.auth.views import LoginView
from django.contrib.auth import views as auth_views
from .views import cerrar_sesion
from . import views


urlpatterns = [
    path('Estudiante', views.Estudiante, name="Estudiante"),#pagina de estudiante
    path('',cerrar_sesion, name="cerrar_sesion"),#para cerrar sesion
#    path('user/<str:username>/', views.user_profile, name='user_profile'),
    path('Estudiante/user/<str:username>/', views.user_profile, name='user_profile'),
    path('login/', auth_views.LoginView.as_view(), name='login'),#para ingresar
    path('login/signup/', views.signup, name='signup'),  # Vista personalizada de registro

]
