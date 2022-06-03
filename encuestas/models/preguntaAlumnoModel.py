from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.deletion import PROTECT

from .encuestaAlumnoModel import encuestaAlumnoModel

POSIBLES_RESPUESTAS = (('Deficiente,Malo,Regular,Bueno,Excelente','Deficiente,Malo,Regular,Bueno,Excelente'),
                       ('Si,No','Si,No'),
                       ('Muy insatisfecho,Insatisfecho,Ni satisfecho ni insatisfecho,Satisfecho,Muy satisfecho',
                        'Muy insatisfecho,Insatisfecho,Ni satisfecho ni insatisfecho,Satisfecho,Muy satisfecho'),
                       ('No aplica,Cumple,Parcialmente,No cumple','No aplica,Cumple,Parcialmente,No cumple'),
                       ('Observacion','Observacion'))

class preguntaAlumnoModel(models.Model):
    pregunta_id = models.AutoField(primary_key=True)
    pregunta = models.CharField(max_length=250,blank=False)
    # valor = models.CharField(max_length=250,blank=False)
    valor = models.CharField(choices=POSIBLES_RESPUESTAS,blank=False,max_length=250)
    orden = models.IntegerField(validators=[MaxValueValidator(100),MinValueValidator(1)])
    encuesta_alumno = models.ForeignKey(encuestaAlumnoModel,on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'PreguntaAlumno'
        db_table = 'pregunta_alumno'
        