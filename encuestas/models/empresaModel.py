from django.db import models

class empresaModel(models.Model):
    empresa_id = models.AutoField(primary_key=True)
    nombre_empresa = models.CharField(max_length=300,blank=False)
    nombre_responsable = models.CharField(max_length=300,blank=False)
    
    class Meta:
        verbose_name = 'empresa'
        db_table = 'empresa'