from turtle import ondrag
from django.db import models

from django.db.models.deletion import PROTECT

from encuestas.models.cursoModel import cursoModel
from encuestas.models.userModel import User

class alumnoModel(models.Model):
    alumno_id = models.AutoField(primary_key=True)
    rut = models.CharField(max_length=10,blank=False,unique=True)
    nombre = models.CharField(max_length=150,blank=False)
    a_paterno = models.CharField(max_length=150,blank=False)
    a_materno = models.CharField(max_length=150,blank=False)
    nombre_completo = models.CharField(max_length=150,blank=False)
    correo = models.CharField(max_length=150)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    curso = models.ForeignKey(cursoModel,on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'alumno'
        db_table = 'alumno'