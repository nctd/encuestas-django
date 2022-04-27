from django.db import models
from django.db.models.deletion import PROTECT


class EncuestaSatisfaccion(models.Model):
    e_id = models.AutoField(primary_key=True)
    fecha_ingreso = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'EncuestaSatisfaccion'
        db_table = 'Encuesta_Satisfaccion'
        
        
class PreguntaSatisfaccion(models.Model):
    pregunta_id = models.AutoField(primary_key=True)
    pregunta = models.CharField(max_length=250,blank=False)
    respuesta = models.CharField(max_length=250,blank=False)
    e = models.ForeignKey(EncuestaSatisfaccion,on_delete=PROTECT)
    
    class Meta:
        verbose_name = 'PreguntaSatisfaccion'
        db_table = 'Pregunta_Satisfaccion'