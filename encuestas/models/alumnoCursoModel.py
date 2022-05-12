from django.db import models
from django.core.exceptions import ValidationError

from encuestas.models.alumnoModel import alumnoModel
from encuestas.models.cursoModel import cursoModel

class alumnoCursoModel(models.Model):
    alumno_curso_id = models.AutoField(primary_key=True)
    alumno = models.ForeignKey(alumnoModel,on_delete=models.CASCADE)
    curso = models.ForeignKey(cursoModel,on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.alumno_curso_id} - {self.alumno} - {self.curso}"
    
    class Meta:
        verbose_name = 'alumno_curso'
        db_table = 'alumno_curso'
        
    def clean(self):
        existe = alumnoCursoModel.objects.filter(alumno=self.alumno,curso=self.curso).exists()
        if existe:
            raise ValidationError('Este alumno ya está asociado al curso')