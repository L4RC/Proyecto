from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User  # Importa el modelo de usuario

class CustomUserCreationForm(UserCreationForm):
    telefono = forms.CharField(max_length=15, required=True)
    dpi = forms.CharField(max_length=15, required=True)
    fecha_nacimiento = forms.DateField(required=True, widget=forms.DateInput(attrs={'type': 'date'}))
    correo = forms.EmailField(max_length=100, required=True)
    nombre = forms.CharField(max_length=100, required=True)
    apellido = forms.CharField(max_length=100, required=True)

    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + ('telefono', 'dpi', 'fecha_nacimiento', 'correo', 'nombre', 'apellido')
