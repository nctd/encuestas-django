from django.db import models

from encuestas.models.cursoModel import cursoModel
from encuestas.models.encuestaSatisfaccionModel import encuestaSatisfaccionModel

class cursoEncuestaModel(models.Model):
    cur_enc_id = models.AutoField(primary_key=True)
    curso = models.ForeignKey(cursoModel,on_delete=models.DO_NOTHING)
    encuesta = models.ForeignKey(encuestaSatisfaccionModel,on_delete=models.DO_NOTHING)
    
    class Meta:
        verbose_name = 'curso_encuesta'
        db_table = 'curso_encuesta'