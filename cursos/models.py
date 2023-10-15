from django.db import models

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

class Seccion(models.Model):#Para agregar el nombre del profesor
    nombre = models.CharField(max_length=50)
    class Meta:
        verbose_name= "Seccion"
        verbose_name_plural = "Secciones"
    def __str__ (self):
        return self.nombre    

class Dia(models.Model):#Para agregar el nombre del profesor
    nombre = models.CharField(max_length=50)
    class Meta:
        verbose_name= "Dia"
        verbose_name_plural = "Dias"
    def __str__ (self):
        return self.nombre  

class Salon(models.Model):#Para agregar el nombre del profesor
    nombre = models.CharField(max_length=50)
    class Meta:
        verbose_name= "Salon"
        verbose_name_plural = "Salones"
    def __str__ (self):
        return self.nombre
    
class Auxiliar(models.Model):#Para agregar el nombre del profesor
    nombre = models.CharField(max_length=50)
    class Meta:
        verbose_name= "Auxiliar"
        verbose_name_plural = "Auxiliar"
    def __str__ (self):
        return self.nombre

class Curso(models.Model):
    Curso = models.ForeignKey(Materia, on_delete=models.CASCADE)
    Seccion = models.ForeignKey(Seccion, on_delete=models.CASCADE)
    Edificio = models.CharField(max_length= 20)
    Salon = models.ForeignKey(Salon, on_delete=models.CASCADE)
    Inicio = models.CharField(max_length= 20)
    Fin = models.CharField(max_length= 20)
    Dias = models.ForeignKey(Dia, on_delete=models.CASCADE)
    Docente = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    Auxiliar = models.ForeignKey(Auxiliar, on_delete=models.CASCADE)