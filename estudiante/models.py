from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
# Create your models here.

class CustomUser(AbstractUser):
    Telefono = models.CharField(max_length=15, blank=True)
    DPI = models.CharField(max_length=15, blank=True)
    Fecha = models.DateField(null=True, blank=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)

    # Agrega related_name para evitar conflictos
    groups = models.ManyToManyField(Group, verbose_name='groups', blank=True, related_name='users_groups')
    user_permissions = models.ManyToManyField(Permission, verbose_name='user permissions', blank=True, related_name='users_permissions')
    # ... otros campos ...
    cursos_inscritos = models.ManyToManyField('cursos.Curso', related_name='inscritos', blank=True)
