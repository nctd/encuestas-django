# Generated by Django 3.2.3 on 2022-05-18 02:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('encuestas', '0005_cursoencuestarecepcionserviciomodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cursoencuestarecepcionserviciomodel',
            name='encuesta_recepcion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='encuestas.encuestarecepcionserviciomodel'),
        ),
    ]
