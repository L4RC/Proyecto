# Generated by Django 4.2.6 on 2023-10-15 05:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0008_auxiliar_salon_alter_curso_salon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='Auxiliar',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cursos.auxiliar'),
        ),
    ]
