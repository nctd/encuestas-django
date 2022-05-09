from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save

from encuestas.models.cursoModel import cursoModel


class encuestaSatisfaccionModel(models.Model):
    encuesta_id = models.AutoField(primary_key=True)
    nombre =  models.CharField(max_length=150,blank=False)
    fecha_creacion = models.DateTimeField(auto_now=True)
    # curso = models.ForeignKey(cursoModel,on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.encuesta_id} - {self.nombre}"
    class Meta:
        verbose_name = 'EncuestaSatisfaccion'
        db_table = 'Encuesta_Satisfaccion'


# @receiver(post_save, sender=cursoModel)   
# def crear_encuesta(sender, instance, created, **kwargs):
#     if created:
#         encuestaSatisfaccionModel.objects.create(curso=instance)