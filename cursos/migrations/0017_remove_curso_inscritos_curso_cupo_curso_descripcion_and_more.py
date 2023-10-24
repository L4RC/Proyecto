# Generated by Django 4.2.6 on 2023-10-24 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estudiante', '0001_initial'),
        ('cursos', '0016_rename_curso_curso_nombre_remove_curso_edificio_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='curso',
            name='inscritos',
        ),
        migrations.AddField(
            model_name='curso',
            name='cupo',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='curso',
            name='descripcion',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='curso',
            name='estudiantes_inscritos',
            field=models.ManyToManyField(blank=True, related_name='estudiantes', to='estudiante.customuser'),
        ),
        migrations.AlterField(
            model_name='curso',
            name='nombre',
            field=models.CharField(max_length=100),
        ),
    ]
