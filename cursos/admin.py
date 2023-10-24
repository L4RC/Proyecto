"""
# cursos/admin.py

from django.contrib import admin
from .models import Curso  # Importa el modelo Curso desde models.py

class CursoAdmin(admin.ModelAdmin):
    # Puedes personalizar la administración del modelo aquí
    list_display = ('nombre', 'cupo', 'descripcion')  # Ejemplo de personalización

# Registra el modelo Curso con la clase de administración personalizada
admin.site.register(Curso, CursoAdmin)
"""
from django.contrib import admin
from .models import Curso  # Asegúrate de que estos nombres coincidan con tus modelos

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'cupo')
    search_fields = ('nombre', 'descripcion')

