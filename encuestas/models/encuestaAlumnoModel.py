from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save

from encuestas.models.alumnoCursoModel import alumnoCursoModel
from encuestas.models.alumnoModel import alumnoModel
from encuestas.models.cursoModel import cursoModel


class encuestaAlumnoModel(models.Model):
    enc_curso_id = models.AutoField(primary_key=True)
    fecha_creacion = models.DateTimeField(auto_now=True)
    alumno_curso = models.ForeignKey(alumnoCursoModel,on_delete=models.PROTECT)
    
    class Meta:
        verbose_name = 'EncuestaAlumno'
        db_table = 'encuesta_alumno'
        
@receiver(post_save, sender=alumnoCursoModel)   
def crear_encuesta(sender, instance, created, **kwargs):
    if created:
        encuestaAlumnoModel.objects.create(alumno_curso=instance)