from django.db import models
from django.db.models.deletion import PROTECT

from .encuestaSatisfaccionModel import encuestaSatisfaccionModel

from .cursoModel import cursoModel


class respuestaSatisfaccionModel(models.Model):
    respuesta_id = models.AutoField(primary_key=True)
    pregunta = models.CharField(max_length=250,blank=False)
    respuesta = models.CharField(max_length=250,blank=False)
    fecha_respuesta = models.DateTimeField(auto_now=True)
    encuesta = models.ForeignKey(encuestaSatisfaccionModel,on_delete=models.CASCADE)
    curso = models.ForeignKey(cursoModel,on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'RespuestaSatisfaccion'
        db_table = 'respuesta_satisfaccion'