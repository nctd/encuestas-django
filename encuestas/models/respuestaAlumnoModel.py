from django.db import models
from django.db.models.deletion import PROTECT

from .encuestaAlumnoModel import encuestaAlumnoModel
from .alumnoModel import alumnoModel


class respuestaAlumnoModel(models.Model):
    respuesta_id = models.AutoField(primary_key=True)
    pregunta = models.CharField(max_length=250,blank=False)
    respuesta = models.CharField(max_length=250,blank=False)
    fecha_respuesta = models.DateTimeField(auto_now=True)
    encuesta_curso = models.ForeignKey(encuestaAlumnoModel,on_delete=models.PROTECT)
    # alumno = models.ForeignKey(alumnoModel,on_delete=models.PROTECT)
    
    class Meta:
        verbose_name = 'RespuestaAlumno'
        db_table = 'respuesta_alumno'