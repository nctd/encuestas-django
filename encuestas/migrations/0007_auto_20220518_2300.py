# Generated by Django 3.2.3 on 2022-05-19 03:00

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('encuestas', '0006_alter_cursoencuestarecepcionserviciomodel_encuesta_recepcion'),
    ]

    operations = [
        migrations.AddField(
            model_name='respuestarecepcionserviciomodel',
            name='porcentaje',
            field=models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='preguntarecepcionserviciomodel',
            name='valor',
            field=models.CharField(choices=[('Deficiente,Malo,Regular,Bueno,Excelente', 'Deficiente,Malo,Regular,Bueno,Excelente'), ('Si,No', 'Si,No'), ('No aplica,Cumple,Parcialmente,No cumple', 'No aplica,Cumple,Parcialmente,No cumple')], max_length=250),
        ),
    ]
