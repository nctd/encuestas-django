from msilib.schema import Error
from django.contrib import messages

from encuestas.models.cursoModel import cursoModel
from encuestas.models.cursoEncuestaRecepcionServicioModel import cursoEncuestaRecepcionServicioModel
from encuestas.models.encuestaRecepcionServicio import encuestaRecepcionServicioModel
from encuestas.models.preguntaAlumnoModel import preguntaAlumnoModel
from encuestas.models.preguntaRecepcionServicio import preguntaRecepcionServicioModel
from encuestas.models.respuestaRecepcionServicioModel import respuestaRecepcionServicioModel

from ...forms import RespuestaAlumnoForm, RespuestaRecepcionServicioForm, RespuestaSatisfaccionForm

def validarRespuestaEncuesta(valor, respuesta):
    posibles_respuestas = valor.split(',')

    if 'Observacion' in posibles_respuestas:
        return True
    if (respuesta in posibles_respuestas):
        return True
    raise Exception

    # return False


def guardarRespuestaEncuestaSatisfaccion(data,encuesta,curso):
    data_resp = {
        'pregunta': data['pregunta'],
        'respuesta_texto': data['respuesta_texto'],
        'respuesta_valor': data['respuesta_valor'],
        'orden_respuesta': data['orden_respuesta'],
        'encuesta' : encuesta,
        'curso' : curso
    }
    
    respuesta = RespuestaSatisfaccionForm(data=data_resp)
    if respuesta.is_valid():
        respuesta.save()

def validarCurso(curso_id,nombre_curso):
    exists = cursoModel.objects.filter(curso_id=curso_id,nombre_curso=nombre_curso).exists()
    if exists: 
        return True 
    return False

def guardarRespuestaEncuestaAlumno(data,encuesta_alumno,alumno_curso):
    data_resp = {
        'pregunta': data['pregunta'],
        'respuesta_texto': data['respuesta_texto'],
        'respuesta_valor': data['respuesta_valor'],
        'orden_respuesta': data['orden_respuesta'],
        'encuesta_alumno' : encuesta_alumno,
        'alumno_curso' : alumno_curso
    }
    
    respuesta = RespuestaAlumnoForm(data=data_resp)
    if respuesta.is_valid():
        respuesta.save()

    
def generarError(render,request,mensaje,status):
    data = {
        'error': True,
        'mensaje': mensaje,
        'status': status
    }
    return render(request, 'error/error.html',data, status=status)       

def obtenerValorRespuesta(respuesta):
    valor = 0
    if(respuesta in ['Deficiente', 'Malo', 'Regular', 'Bueno', 'Excelente', 'Si','No','No aplica','Cumple','Parcialmente','No cumple']):
        if respuesta == 'Deficiente': valor = 1
        if respuesta == 'Malo': valor = 2
        if respuesta == 'Regular': valor = 3
        if respuesta == 'Bueno': valor = 4
        if respuesta == 'Excelente': valor = 5
        if respuesta == 'Si': valor = 1
        if respuesta == 'No': valor = 0
        if respuesta == 'No aplica': valor = 0
        if respuesta == 'Cumple': valor = 5
        if respuesta == 'Parcialmente': valor = 3
        if respuesta == 'No cumple': valor = 0
    return valor 


def guardarRespuestaEncuestaRecepcionServicio(data,encuesta,curso):
    data_resp = {
        'pregunta': data['pregunta'],
        'respuesta_texto': data['respuesta_texto'],
        'respuesta_valor': data['respuesta_valor'],
        'orden_respuesta': data['orden_respuesta'],
        'encuesta_recepcion' : encuesta,
        'curso' : curso,
        'porcentaje': data['porcentaje']
    }
    
    respuesta = RespuestaRecepcionServicioForm(data=data_resp)
    if respuesta.is_valid():
        respuesta.save()    
        

def obtenerResultadoRecepcionServicio(encuesta_id,curso_id):
    respuestas = respuestaRecepcionServicioModel.objects.filter(curso_id=curso_id,encuesta_recepcion_id=encuesta_id)
    ponderado = 0
    ponderado = sum((value.respuesta_valor*value.porcentaje/100) for value in respuestas)
    return ponderado