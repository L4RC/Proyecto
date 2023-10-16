#from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class CustomUser(AbstractUser):
    Nombre = models.CharField(max_length= 30,default='')
    Apellido = models.CharField(max_length= 30, default='')
    DPI = models.CharField(max_length= 13, default='')
    Fecha = models.CharField(max_length= 100)
    Telefono = models.CharField(max_length= 100, default='')
    Usuario = models.CharField(max_length= 15,unique=True)
    Correo = models.EmailField(unique=True)

    groups = models.ManyToManyField(Group, related_name='customuser_set')
    user_permissions = models.ManyToManyField(Permission, related_name='customuser_set')


    def __str__(self):
        return self.username
