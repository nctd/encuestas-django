from django.db import models

from encuestas.models.userModel import User

class empresaModel(models.Model):
    empresa_id = models.AutoField(primary_key=True)
    nombre_empresa = models.CharField(max_length=300,blank=False)
    nombre_responsable = models.CharField(max_length=300,blank=False)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.nombre_empresa} - {self.nombre_responsable}"
    
    class Meta:
        verbose_name = 'empresa'
        db_table = 'empresa'