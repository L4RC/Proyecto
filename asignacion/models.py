from django.db import models

# Create your models here.

class assignment(models.Model):
    Curso = models.CharField(max_length=50)
    Seccion = models.CharField(max_length=10)
    Edificio = models.CharField(max_length= 20)
    Salon = models.CharField(max_length= 20)
    Inicio = models.CharField(max_length= 20)
    Fin = models.CharField(max_length= 20)
    Dias = models.CharField(max_length= 20)
    Docente = models.CharField(max_length= 80)
    Auxiliar = models.CharField(max_length= 80)