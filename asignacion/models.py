from django.db import models

# Create your models here. Para la asignación de cursos
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

class Seccion(models.Model):#Para agregar el nombre del profesor
    nombre = models.CharField(max_length=50)
    class Meta:
        verbose_name= "Seccion"
        verbose_name_plural = "Secciones"
    def __str__ (self):
        return self.nombre    


class Categoria(models.Model):
    Curso = models.ForeignKey(Materia, on_delete=models.CASCADE)
    Seccion = models.ForeignKey(Seccion, on_delete=models.CASCADE)
    Edificio = models.CharField(max_length= 20)
    Salon = models.CharField(max_length= 20)
    Inicio = models.CharField(max_length= 20)
    Fin = models.CharField(max_length= 20)
    Dias = models.CharField(max_length= 20)
    Docente = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    Auxiliar = models.CharField(max_length= 80)
    Precio = models.CharField(max_length=20)
    Disponibilidad = models.BooleanField(default=True)

    class Meta:
        verbose_name= "Categoria"
        verbose_name_plural = "Categorias"

    def __str__ (self):
        return self.Curso
    
