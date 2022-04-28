from django.db import models
from django.db.models.deletion import PROTECT

from .encuestaSatisfaccionModel import encuestaSatisfaccionModel



class preguntaSatisfaccionModel(models.Model):
    pregunta_id = models.AutoField(primary_key=True)
    pregunta = models.CharField(max_length=250,blank=False)
    respuesta = models.CharField(max_length=250,blank=False)
    e = models.ForeignKey(encuestaSatisfaccionModel,on_delete=PROTECT)
    
    class Meta:
        verbose_name = 'PreguntaSatisfaccion'
        db_table = 'Pregunta_Satisfaccion'