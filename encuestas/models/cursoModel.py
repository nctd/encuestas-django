from django.db import models

from encuestas.models.empresaModel import empresaModel

class cursoModel(models.Model):
    curso_id = models.AutoField(primary_key=True)
    nombre_curso = models.CharField(max_length=300,blank=False)
    fecha_inicio = models.DateField(blank=False)
    fecha_termino = models.DateField(blank=False)
    resp_cliente = models.ForeignKey(empresaModel,on_delete=models.DO_NOTHING)
    resp_exsol = models.CharField(max_length=300,blank=False)
    contrato = models.CharField(max_length=100,blank=False)
    req_servicio = models.CharField(max_length=300,blank=False)
    
    
    class Meta:
        verbose_name = 'curso'
        db_table = 'curso'