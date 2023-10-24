# Generated by Django 4.2.6 on 2023-10-24 05:03

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cursos', '0017_remove_curso_inscritos_curso_cupo_curso_descripcion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='estudiantes_inscritos',
            field=models.ManyToManyField(blank=True, related_name='estudiantes', to=settings.AUTH_USER_MODEL),
        ),
    ]
