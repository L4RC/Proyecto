# Generated by Django 4.2.6 on 2023-10-14 05:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0005_alter_curso_curso_alter_curso_docente_delete_materia_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Materia',
                'verbose_name_plural': 'Materias',
            },
        ),
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Profesor',
                'verbose_name_plural': 'Profesores',
            },
        ),
        migrations.AlterField(
            model_name='curso',
            name='Curso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cursos.materia'),
        ),
        migrations.AlterField(
            model_name='curso',
            name='Docente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cursos.profesor'),
        ),
    ]