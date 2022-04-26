from django.db import models
from django.db.models.deletion import PROTECT


class EncuestaSatisfaccion(models.Model):
    e_id = models.AutoField(primary_key=True)
    class Meta:
        verbose_name = 'EncuestaSatisfaccion'
        db_table = 'Encuesta_Satisfaccion'
        
        
class PreguntaSatisfaccion(models.Model):
    pregunta_id = models.AutoField(primary_key=True)
    pregunta = models.TextField()
    respuesta = models.CharField(max_length=70,blank=False)
    encuesta_satisfaccion = models.ForeignKey(EncuestaSatisfaccion,on_delete=PROTECT)
    
    class Meta:
        verbose_name = 'PreguntaSatisfaccion'
        db_table = 'Pregunta_Satisfaccion'