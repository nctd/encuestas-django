from django.db import models
from django.core.exceptions import ValidationError

from encuestas.models.cursoModel import cursoModel
from encuestas.models.encuestaAlumnoModel import encuestaAlumnoModel

class cursoEncuestaAlumnoModel(models.Model):
    curso_encuesta_alumno_id = models.AutoField(primary_key=True)
    curso = models.ForeignKey(cursoModel,on_delete=models.CASCADE)
    encuesta = models.ForeignKey(encuestaAlumnoModel,on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.curso} - {self.encuesta}"

    
    class Meta:
        verbose_name = 'curso_encuesta_alumno'
        db_table = 'curso_encuesta_alumno'
        
    def clean(self):
        existe = cursoEncuestaAlumnoModel.objects.filter(curso=self.curso,encuesta=self.encuesta).exists()
        if existe:
            raise ValidationError('Esta encuesta ya está asociada al curso')