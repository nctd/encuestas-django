from django.db import models
from django.db.models.deletion import PROTECT
from django.core.validators import MaxValueValidator, MinValueValidator

from encuestas.models.encuestaRecepcionServicio import encuestaRecepcionServicioModel
from .cursoModel import cursoModel


class respuestaRecepcionServicioModel(models.Model):
    respuesta_id = models.AutoField(primary_key=True)
    pregunta = models.CharField(max_length=250,blank=False)
    respuesta_texto = models.CharField(max_length=250,blank=True,default='0')
    respuesta_valor = models.IntegerField(validators=[MaxValueValidator(5),MinValueValidator(0)])
    fecha_respuesta = models.DateTimeField(auto_now=True)
    orden_respuesta = models.IntegerField()
    encuesta_recepcion = models.ForeignKey(encuestaRecepcionServicioModel,on_delete=models.CASCADE)
    curso = models.ForeignKey(cursoModel,on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'RespuestaRecepcionServicio'
        db_table = 'respuesta_recepcion_servicio'