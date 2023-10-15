from django.contrib import admin
from .models import Categoria, Materia, Profesor
# Register your models here.


admin.site.register(Materia)
admin.site.register(Profesor)
admin.site.register(Categoria)

