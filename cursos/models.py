from django.db import models
from django.contrib.auth.models import User

class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    cupo = models.PositiveIntegerField()
    estudiantes_inscritos = models.ManyToManyField(User, related_name='cursos_inscritos', blank=True)

class Estudiante(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Otros campos específicos del estudiante, como el número de teléfono, pueden ir aquí

"""
# Create your models here.
class Materia(models.Model):#Para agregar la materia
    nombre = models.CharField(max_length=50)
    class Meta:
        verbose_name= "Materia"
        verbose_name_plural = "Materias"
    def __str__ (self):
        return self.nombre

class Profesor(models.Model):#Para agregar el nombre del profesor
    nombre = models.CharField(max_length=50)
    class Meta:
        verbose_name= "Profesor"
        verbose_name_plural = "Profesores"
    def __str__ (self):
        return self.nombre    
    
class Auxiliar(models.Model):#Para agregar el nombre del auxiliar
    nombre = models.CharField(max_length=50)
    class Meta:
        verbose_name= "Auxiliar"
        verbose_name_plural = "Auxiliar"
    def __str__ (self):
        return self.nombre
    
class Precio(models.Model):
    nombre = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    class Meta:
        verbose_name = "Precio"
        verbose_name_plural = "Precios"
    def __str__(self):
        return str(self.nombre)  # Convierte el objeto decimal en una cadena


class Curso(models.Model):#Para agregar los cursos, titulo, nombre, docente, aux, seccion
    Curso = models.ForeignKey(Materia, on_delete=models.CASCADE)
    Edificio = models.CharField(max_length= 20)
    Docente = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    Auxiliar = models.ForeignKey(Auxiliar, on_delete=models.CASCADE)
    Precio = models.ForeignKey(Precio, on_delete=models.CASCADE)
"""
