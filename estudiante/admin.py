from django.contrib import admin
from .models import CustomUser  # Asegúrate de que estos nombres coincidan con tus modelos


# Register your models here.
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'nombre', 'apellido')
    search_fields = ('username', 'email', 'nombre', 'apellido')