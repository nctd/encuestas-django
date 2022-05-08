from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save

from encuestas.models.alumnoCursoModel import alumnoCursoModel
from encuestas.models.cursoModel import cursoModel


class encuestaCursoModel(models.Model):
    e_curso_id = models.AutoField(primary_key=True)
    fecha_creacion = models.DateTimeField(auto_now=True)
    curso = models.ForeignKey(cursoModel,on_delete=models.PROTECT)
    
    class Meta:
        verbose_name = 'EncuestaCurso'
        db_table = 'encuesta_curso'
        
@receiver(post_save, sender=alumnoCursoModel)   
def crear_encuesta(sender, instance, created, **kwargs):
    if created:
        encuestaCursoModel.objects.create(curso_id=instance.curso_id)