from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    es_empresa = models.BooleanField(default=False)
    es_alumno = models.BooleanField(default=False)
    
    class Meta:
        db_table = 'users'