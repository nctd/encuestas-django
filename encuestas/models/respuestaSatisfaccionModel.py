from django.db import models
from django.db.models.deletion import PROTECT

from .encuestaSatisfaccionModel import encuestaSatisfaccionModel

from .cursoModel import cursoModel


class respuestaSatisfaccionModel(models.Model):
    respuesta_id = models.AutoField(primary_key=True)
    pregunta = models.CharField(max_length=250,blank=False)
    respuesta = models.CharField(max_length=250,blank=False)
    encuesta = models.ForeignKey(encuestaSatisfaccionModel,on_delete=models.PROTECT)
    curso = models.ForeignKey(cursoModel,on_delete=models.PROTECT)
    
    class Meta:
        verbose_name = 'RespuestaSatisfaccion'
        db_table = 'respuesta_satisfaccion'