from django.db import models
from django.db.models.deletion import PROTECT
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.validators import MaxValueValidator, MinValueValidator

from .encuestaSatisfaccionModel import encuestaSatisfaccionModel

POSIBLES_RESPUESTAS = (('Deficiente,Malo,Regular,Bueno,Excelente','Deficiente,Malo,Regular,Bueno,Excelente'),
                       ('Si,No','Si,No'),
                       ('Muy insatisfecho,Insatisfecho,Ni satisfecho ni insatisfecho,Satisfecho,Muy satisfecho',
                        'Muy insatisfecho,Insatisfecho,Ni satisfecho ni insatisfecho,Satisfecho,Muy satisfecho'),
                       ('No aplica,Cumple,Parcialmente,No cumple','No aplica,Cumple,Parcialmente,No cumple'),
                       ('Observacion','Observacion'))

class preguntaSatisfaccionModel(models.Model):
    pregunta_id = models.AutoField(primary_key=True)
    pregunta = models.CharField(max_length=250,blank=False)
    valor = models.CharField(choices=POSIBLES_RESPUESTAS,blank=False,max_length=250)
    orden = models.IntegerField(validators=[MaxValueValidator(100),MinValueValidator(1)])
    encuesta = models.ForeignKey(encuestaSatisfaccionModel,on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'PreguntaSatisfaccion'
        db_table = 'Pregunta_Satisfaccion'
        