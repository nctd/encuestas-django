from django.db import models

from encuestas.models.cursoModel import cursoModel


class encuestaCursoModel(models.Model):
    e_curso_id = models.AutoField(primary_key=True)
    fecha_creacion = models.DateTimeField(auto_now=True)
    curso_id = models.ForeignKey(cursoModel,on_delete=models.PROTECT)
    
    class Meta:
        verbose_name = 'EncuestaCurso'
        db_table = 'encuesta_curso'
        
        