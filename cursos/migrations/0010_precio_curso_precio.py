# Generated by Django 4.2.6 on 2023-10-18 07:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0009_alter_curso_auxiliar'),
    ]

    operations = [
        migrations.CreateModel(
            name='Precio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
            ],
            options={
                'verbose_name': 'Precio',
                'verbose_name_plural': 'Precios',
            },
        ),
        migrations.AddField(
            model_name='curso',
            name='Precio',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='cursos.precio'),
            preserve_default=False,
        ),
    ]
