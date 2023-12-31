# Generated by Django 4.2.6 on 2023-10-14 03:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('asignacion', '0003_categoria_delete_assignment'),
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
                'verbose_name': 'Materia',
                'verbose_name_plural': 'Materias',
            },
        ),
        migrations.AlterField(
            model_name='categoria',
            name='Curso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asignacion.materia'),
        ),
        migrations.AlterField(
            model_name='categoria',
            name='Docente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asignacion.profesor'),
        ),
    ]
