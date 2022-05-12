from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.deletion import PROTECT

from .encuestaAlumnoModel import encuestaAlumnoModel

class preguntaAlumnoModel(models.Model):
    pregunta_id = models.AutoField(primary_key=True)
    pregunta = models.CharField(max_length=250,blank=False)
    valor = models.CharField(max_length=250,blank=False)
    orden = models.IntegerField(validators=[MaxValueValidator(100),MinValueValidator(1)])
    encuesta_curso = models.ForeignKey(encuestaAlumnoModel,on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'PreguntaAlumno'
        db_table = 'pregunta_alumno'
        
# @receiver(post_save, sender=encuestaAlumnoModel)   
# def crear_preguntas(sender, instance, created, **kwargs):
#     if created:
#         preguntaAlumnoModel.objects.create(pregunta='¿Se cumplieron los objetivos del curso?',
#                                                  valor='Deficiente,Malo,Regular,Bueno,Excelente',
#                                                  orden = 1,
#                                                  encuesta_curso=instance)
#         preguntaAlumnoModel.objects.create(pregunta='¿El contenido del curso fue interesante e importante para su trabajo?',
#                                                  valor='Deficiente,Malo,Regular,Bueno,Excelente',
#                                                  orden = 2,
#                                                  encuesta_curso=instance)
#         preguntaAlumnoModel.objects.create(pregunta='Intercambio de experiencias entre los participantes',
#                                                  valor='Deficiente,Malo,Regular,Bueno,Excelente',
#                                                  orden = 3,
#                                                  encuesta_curso=instance)
#         preguntaAlumnoModel.objects.create(pregunta='Dinámica del curso',
#                                                  valor='Deficiente,Malo,Regular,Bueno,Excelente',
#                                                  orden = 4,
#                                                  encuesta_curso=instance)
#         preguntaAlumnoModel.objects.create(pregunta='Ambiente de Trabajo',
#                                                  valor='Deficiente,Malo,Regular,Bueno,Excelente',
#                                                  orden = 5,
#                                                  encuesta_curso=instance)
#         preguntaAlumnoModel.objects.create(pregunta='Comunicación y dominio de los contenidos por parte del Relator',
#                                                  valor='Deficiente,Malo,Regular,Bueno,Excelente',
#                                                  orden = 6,
#                                                  encuesta_curso=instance)
#         preguntaAlumnoModel.objects.create(pregunta='Puntualidad del Relator',
#                                                  valor='Deficiente,Malo,Regular,Bueno,Excelente',
#                                                  orden = 7,
#                                                  encuesta_curso=instance)
#         preguntaAlumnoModel.objects.create(pregunta='Calidad de su manual de trabajo',
#                                                  valor='Deficiente,Malo,Regular,Bueno,Excelente',
#                                                  orden = 8,
#                                                  encuesta_curso=instance)
#         preguntaAlumnoModel.objects.create(pregunta='Proyección de la Clase (Contenidos, nitidez, colores)',
#                                                  valor='Deficiente,Malo,Regular,Bueno,Excelente',
#                                                  orden = 9,
#                                                  encuesta_curso=instance)
#         preguntaAlumnoModel.objects.create(pregunta='Que le pareció el trato que recibió como cliente',
#                                                  valor='Deficiente,Malo,Regular,Bueno,Excelente',
#                                                  orden = 10,
#                                                  encuesta_curso=instance)
#         preguntaAlumnoModel.objects.create(pregunta='Instalaciones (Infraestructura)',
#                                                  valor='Deficiente,Malo,Regular,Bueno,Excelente',
#                                                  orden = 11,
#                                                  encuesta_curso=instance)
#         preguntaAlumnoModel.objects.create(pregunta='Servicio de Alimentación',
#                                                  valor='Deficiente,Malo,Regular,Bueno,Excelente',
#                                                  orden = 12,
#                                                  encuesta_curso=instance)
#         preguntaAlumnoModel.objects.create(pregunta='Estimado(a) Participante, si desea agregar algún comentario, que sería de gran utilidad para nosotros, puede escribirlo a continuación:',
#                                                  valor='Observacion',
#                                                  orden = 13,
#                                                  encuesta_curso=instance)