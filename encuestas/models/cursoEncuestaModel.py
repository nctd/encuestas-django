from django.db import models
from django.core.exceptions import ValidationError

from encuestas.models.cursoModel import cursoModel
from encuestas.models.encuestaSatisfaccionModel import encuestaSatisfaccionModel

class cursoEncuestaModel(models.Model):
    cur_enc_id = models.AutoField(primary_key=True)
    curso = models.ForeignKey(cursoModel,on_delete=models.CASCADE)
    encuesta = models.ForeignKey(encuestaSatisfaccionModel,on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'curso_encuesta'
        db_table = 'curso_encuesta'
        
    def clean(self):
        existe = cursoEncuestaModel.objects.filter(curso=self.curso,encuesta=self.encuesta).exists()
        if existe:
            raise ValidationError('Esta encuesta ya está asociada al curso')