from django.db import models

class catalogoModel(models.Model):
    id_catalogo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=300,blank=False)
    pregunta = models.CharField(max_length=300,blank=False)
    opciones = models.CharField(max_length=300,blank=False)
    tipo = models.CharField(max_length=300,blank=False)
    orden = models.IntegerField()
    
    class Meta:
        verbose_name = 'catalogo'
        db_table = 'catalogo'