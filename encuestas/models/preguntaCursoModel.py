from django.db import models
from django.db.models.deletion import PROTECT

from .encuestaCursoModel import encuestaCursoModel
from .alumnoModel import alumnoModel


class preguntaCursoModel(models.Model):
    pregunta_id = models.AutoField(primary_key=True)
    pregunta = models.CharField(max_length=250,blank=False)
    respuesta = models.CharField(max_length=250,blank=False)
    e_curso = models.ForeignKey(encuestaCursoModel,on_delete=models.PROTECT)
    alumno = models.ForeignKey(alumnoModel,on_delete=models.PROTECT)
    
    class Meta:
        verbose_name = 'PreguntaCurso'
        db_table = 'pregunta_curso'