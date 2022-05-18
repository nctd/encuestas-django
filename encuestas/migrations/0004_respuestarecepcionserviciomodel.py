# Generated by Django 3.2.3 on 2022-05-18 02:05

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('encuestas', '0003_rename_encuesta_preguntarecepcionserviciomodel_encuesta_recepcion'),
    ]

    operations = [
        migrations.CreateModel(
            name='respuestaRecepcionServicioModel',
            fields=[
                ('respuesta_id', models.AutoField(primary_key=True, serialize=False)),
                ('pregunta', models.CharField(max_length=250)),
                ('respuesta_texto', models.CharField(blank=True, default='0', max_length=250)),
                ('respuesta_valor', models.IntegerField(validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)])),
                ('fecha_respuesta', models.DateTimeField(auto_now=True)),
                ('orden_respuesta', models.IntegerField()),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='encuestas.cursomodel')),
                ('encuesta_recepcion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='encuestas.encuestarecepcionserviciomodel')),
            ],
            options={
                'verbose_name': 'RespuestaRecepcionServicio',
                'db_table': 'respuesta_recepcion_servicio',
            },
        ),
    ]
