from django.db import models
from django.core.exceptions import ValidationError

from encuestas.models.cursoModel import cursoModel
from encuestas.models.encuestaSatisfaccionModel import encuestaSatisfaccionModel

class cursoEncuestaSatisfaccionModel(models.Model):
    curso_encuesta_id = models.AutoField(primary_key=True)
    curso = models.ForeignKey(cursoModel,on_delete=models.CASCADE)
    encuesta = models.ForeignKey(encuestaSatisfaccionModel,on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'curso_encuesta_satisfaccion'
        db_table = 'curso_encuesta_satisfaccion'
        
    def clean(self):
        existe = cursoEncuestaSatisfaccionModel.objects.filter(curso=self.curso,encuesta=self.encuesta).exists()
        if existe:
            raise ValidationError('Esta encuesta ya está asociada al curso')