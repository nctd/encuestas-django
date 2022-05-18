from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save



class encuestaRecepcionServicioModel(models.Model):
    encuesta_recepcion_id = models.AutoField(primary_key=True)
    nombre =  models.CharField(max_length=150,blank=False)
    fecha_creacion = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.encuesta_recepcion_id} - {self.nombre}"
    
    class Meta:
        verbose_name = 'EncuestaRecepcionServicio'
        db_table = 'encuesta_recepcion_servicio'
