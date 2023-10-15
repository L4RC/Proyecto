# Generated by Django 4.2.6 on 2023-10-14 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asignacion', '0002_rename_asig_assignment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
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
                ('Precio', models.CharField(max_length=20)),
                ('Disponibilidad', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
            },
        ),
        migrations.DeleteModel(
            name='assignment',
        ),
    ]
