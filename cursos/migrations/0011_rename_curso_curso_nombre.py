# Generated by Django 4.2.6 on 2023-10-19 07:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0010_precio_curso_precio'),
    ]

    operations = [
        migrations.RenameField(
            model_name='curso',
            old_name='Curso',
            new_name='Nombre',
        ),
    ]
