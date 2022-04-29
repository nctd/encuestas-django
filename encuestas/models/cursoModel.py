from django.db import models

class cursoModel(models.Model):
    curso_id = models.AutoField(primary_key=True)
    nombre_curso = models.CharField(max_length=300,blank=False)
    fecha_inicio = models.DateField(blank=False)
    fecha_termino = models.DateField(blank=False)
    
    class Meta:
        verbose_name = 'curso'
        db_table = 'curso'