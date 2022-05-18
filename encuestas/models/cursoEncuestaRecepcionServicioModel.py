from django.db import models
from django.core.exceptions import ValidationError

from encuestas.models.cursoModel import cursoModel
from encuestas.models.encuestaRecepcionServicio import encuestaRecepcionServicioModel


class cursoEncuestaRecepcionServicioModel(models.Model):
    curso_encuesta_recepcion_id = models.AutoField(primary_key=True)
    curso = models.ForeignKey(cursoModel,on_delete=models.CASCADE)
    encuesta_recepcion = models.ForeignKey(encuestaRecepcionServicioModel,on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.curso} - {self.encuesta_recepcion}"
    
    class Meta:
        verbose_name = 'curso_encuesta_recepcion_servicio'
        db_table = 'curso_encuesta_recepcion_servicio'
        
    def clean(self):
        existe = cursoEncuestaRecepcionServicioModel.objects.filter(curso=self.curso,encuesta_recepcion=self.encuesta_recepcion).exists()
        if existe:
            raise ValidationError('Esta encuesta ya está asociada al curso')