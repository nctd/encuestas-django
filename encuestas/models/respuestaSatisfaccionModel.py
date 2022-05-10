from django.db import models
from django.db.models.deletion import PROTECT
from django.core.validators import MaxValueValidator, MinValueValidator

from .encuestaSatisfaccionModel import encuestaSatisfaccionModel

from .cursoModel import cursoModel


class respuestaSatisfaccionModel(models.Model):
    respuesta_id = models.AutoField(primary_key=True)
    pregunta = models.CharField(max_length=250,blank=False)
    respuesta_texto = models.CharField(max_length=250,blank=False)
    respuesta_valor = models.IntegerField(validators=[MaxValueValidator(5),MinValueValidator(0)])
    fecha_respuesta = models.DateTimeField(auto_now=True)
    orden_respuesta = models.IntegerField()
    encuesta = models.ForeignKey(encuestaSatisfaccionModel,on_delete=models.CASCADE)
    curso = models.ForeignKey(cursoModel,on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'RespuestaSatisfaccion'
        db_table = 'respuesta_satisfaccion'