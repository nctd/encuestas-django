from django.db import models

from encuestas.models.alumnoModel import alumnoModel
from encuestas.models.cursoModel import cursoModel

class alumnoCursoModel(models.Model):
    al_cu_id = models.AutoField(primary_key=True)
    alumno = models.ForeignKey(alumnoModel,on_delete=models.PROTECT)
    curso = models.ForeignKey(cursoModel,on_delete=models.PROTECT)
    
    class Meta:
        verbose_name = 'alumno_curso'
        db_table = 'alumno_curso'