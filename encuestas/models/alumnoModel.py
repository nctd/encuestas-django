from turtle import ondrag
from django.db import models
from django.db.models.deletion import PROTECT

from .cursoModel import cursoModel

class alumnoModel(models.Model):
    alumno_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=150,blank=False)
    a_paterno = models.CharField(max_length=150,blank=False)
    a_materno = models.CharField(max_length=150,blank=False)
    correo = models.CharField(max_length=150,blank=False)
    curso = models.ForeignKey(cursoModel,on_delete=models.PROTECT)
    
    class Meta:
        verbose_name = 'alumno'
        db_table = 'alumno'