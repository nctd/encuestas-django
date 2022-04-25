from django.db import models

class EncuestaSatisfaccion(models.Model):
    e_id = models.AutoField(primary_key=True)
    pregunta_1 = models.TextField()
    respuesta_1 = models.CharField(max_length=70,blank=False)
    
    class Meta:
        verbose_name = 'Encuesta'
        db_table = 'Encuesta'