# Generated by Django 4.2.6 on 2023-10-10 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cursos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Curso', models.CharField(max_length=50)),
                ('Seccion', models.CharField(max_length=10)),
                ('Edificio', models.CharField(max_length=20)),
                ('Salon', models.CharField(max_length=20)),
                ('Inicio', models.CharField(max_length=20)),
                ('Fin', models.CharField(max_length=20)),
                ('Dias', models.CharField(max_length=20)),
                ('Docente', models.CharField(max_length=80)),
                ('Auxiliar', models.CharField(max_length=80)),
            ],
            options={
                'verbose_name': 'curso',
                'verbose_name_plural': 'cursos',
            },
        ),
    ]
