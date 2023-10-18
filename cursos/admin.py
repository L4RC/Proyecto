from django.contrib import admin
from .models import Curso, Materia, Profesor, Seccion, Dia, Salon, Auxiliar, Precio

# Register your models here.

class CursosAdmin(admin.ModelAdmin):
    readonly_fields = ['created','updated']

admin.site.register(Curso)
admin.site.register(Materia)
admin.site.register(Profesor)
admin.site.register(Seccion)
admin.site.register(Dia)
admin.site.register(Salon)
admin.site.register(Auxiliar)
admin.site.register(Precio)