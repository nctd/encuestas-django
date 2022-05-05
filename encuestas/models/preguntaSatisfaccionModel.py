from statistics import mode
from django.db import models
from django.db.models.deletion import PROTECT
from django.dispatch import receiver
from django.db.models.signals import post_save
from .encuestaSatisfaccionModel import encuestaSatisfaccionModel



class preguntaSatisfaccionModel(models.Model):
    pregunta_id = models.AutoField(primary_key=True)
    pregunta = models.CharField(max_length=250,blank=False)
    valor = models.CharField(max_length=250,blank=False)
    orden = models.IntegerField()
    encuesta = models.ForeignKey(encuestaSatisfaccionModel,on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'PreguntaSatisfaccion'
        db_table = 'Pregunta_Satisfaccion'
        
        
@receiver(post_save, sender=encuestaSatisfaccionModel)   
def crear_encuesta(sender, instance, created, **kwargs):
    if created:
        preguntaSatisfaccionModel.objects.create(pregunta='¿Cómo fue la atención general que se le brindó?',
                                                 valor='Deficiente,Malo,Regular,Bueno,Excelente',
                                                 orden = 1,
                                                 encuesta=instance)
        preguntaSatisfaccionModel.objects.create(pregunta='¿Se demostró conocimiento del o los servicios ofrecidos?',
                                                 valor='Deficiente,Malo,Regular,Bueno,Excelente',
                                                 orden = 2,
                                                 encuesta=instance)
        preguntaSatisfaccionModel.objects.create(pregunta='¿La persona administrativa, contestó de forma rápida y adecuada sus inquietudes?',
                                                 valor='Deficiente,Malo,Regular,Bueno,Excelente',
                                                 orden = 3,
                                                 encuesta=instance)
        preguntaSatisfaccionModel.objects.create(pregunta='¿Qué le pareció el servicio en general brindado?',
                                                 valor='Deficiente,Malo,Regular,Bueno,Excelente',
                                                 orden = 4,
                                                 encuesta=instance)
        preguntaSatisfaccionModel.objects.create(pregunta='¿Recomendaría al organismo de capacitación?',
                                                 valor='Si,No',
                                                 orden = 5,
                                                 encuesta=instance)
        preguntaSatisfaccionModel.objects.create(pregunta='¿Compraría otro servicio al organismo?',
                                                 valor='Si,No',
                                                 orden = 6,
                                                 encuesta=instance)
        preguntaSatisfaccionModel.objects.create(pregunta='¿El servicio prestado, cumplió con sus expectativas?',
                                                 valor='Si,No',
                                                 orden = 7,
                                                 encuesta=instance)
        preguntaSatisfaccionModel.objects.create(pregunta='¿Se cumplió con lo planificado en el Servicio?',
                                                 valor='Si,No',
                                                 orden = 8,
                                                 encuesta=instance)
        preguntaSatisfaccionModel.objects.create(pregunta='¿Qué otros cursos le gustarían tomar?',
                                                 valor='Observacion',
                                                 orden = 9,
                                                 encuesta=instance)