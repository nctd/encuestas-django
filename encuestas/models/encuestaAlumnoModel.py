from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save

from encuestas.models.alumnoCursoModel import alumnoCursoModel
from encuestas.models.alumnoModel import alumnoModel
from encuestas.models.cursoModel import cursoModel


class encuestaAlumnoModel(models.Model):
    encuesta_alumno_id = models.AutoField(primary_key=True)
    nombre =  models.CharField(max_length=150,blank=False)
    fecha_creacion = models.DateTimeField(auto_now=True)
    # alumno_curso = models.ForeignKey(alumnoCursoModel,on_delete=models.PROTECT)
    
    def __str__(self):
        return f"{self.encuesta_alumno_id} - {self.nombre}"
    
    class Meta:
        verbose_name = 'EncuestaAlumno'
        db_table = 'encuesta_alumno'
        
# @receiver(post_save, sender=alumnoCursoModel)   
# def crear_encuesta(sender, instance, created, **kwargs):
#     if created:
#         encuestaAlumnoModel.objects.create(alumno_curso=instance)