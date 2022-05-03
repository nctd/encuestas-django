from django.db import models


class encuestaSatisfaccionModel(models.Model):
    encuesta_id = models.AutoField(primary_key=True)
    fecha_creacion = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'EncuestaSatisfaccion'
        db_table = 'Encuesta_Satisfaccion'
        
        