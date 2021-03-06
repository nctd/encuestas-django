from django.db.models import Avg,Sum,Count,Value

from encuestas.models.cursoModel import cursoModel
from encuestas.models.cursoEncuestaRecepcionServicioModel import cursoEncuestaRecepcionServicioModel
from encuestas.models.encuestaRecepcionServicio import encuestaRecepcionServicioModel
from encuestas.models.preguntaAlumnoModel import preguntaAlumnoModel
from encuestas.models.preguntaRecepcionServicio import preguntaRecepcionServicioModel
from encuestas.models.respuestaAlumnoModel import respuestaAlumnoModel
from encuestas.models.respuestaRecepcionServicioModel import respuestaRecepcionServicioModel
from encuestas.models.respuestaSatisfaccionModel import respuestaSatisfaccionModel

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

def guardarRespuestaEncuestaAlumno(data,encuesta_alumno,alumno_curso,curso):
    data_resp = {
        'pregunta': data['pregunta'],
        'respuesta_texto': data['respuesta_texto'],
        'respuesta_valor': data['respuesta_valor'],
        'orden_respuesta': data['orden_respuesta'],
        'encuesta_alumno' : encuesta_alumno,
        'alumno_curso' : alumno_curso,
        'curso':curso
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
    if(respuesta in ['Deficiente','Malo','Regular','Bueno','Excelente','Si','No',
                     'Muy insatisfecho','Insatisfecho','Ni satisfecho ni insatisfecho','Satisfecho','Muy satisfecho',
                     'No aplica','Cumple','Parcialmente','No cumple','No aplica','Cumple','Parcialmente','No cumple','Observacion']):
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
        if respuesta == 'Muy insatisfecho': valor = 1
        if respuesta == 'Insatisfecho': valor  = 2
        if respuesta == 'Ni satisfecho ni insatisfecho': valor  = 3
        if respuesta == 'Satisfecho': valor  = 4
        if respuesta == 'Muy satisfecho': valor  = 5

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
    preguntas = preguntaRecepcionServicioModel.objects.filter(encuesta_recepcion_id=encuesta_id)
    esperado = 0
    esperado = sum((value.porcentaje*5/100) for value in preguntas)

    respuestas = respuestaRecepcionServicioModel.objects.filter(curso_id=curso_id,encuesta_recepcion_id=encuesta_id)
    ponderado = 0
    ponderado = sum((value.respuesta_valor*value.porcentaje/100) for value in respuestas)

    return round((ponderado*100)/esperado)


def obtenerPromedioEncuesta(encuesta_id,curso_id,tipo,excluir):
    if tipo == 'alumno':
        return respuestaAlumnoModel.objects.filter(curso=curso_id,encuesta_alumno_id=encuesta_id).values('pregunta','curso_id').annotate(promedio=Avg('respuesta_valor')).exclude(pregunta__in=excluir)
    if tipo == 'satisfaccion':
        return respuestaSatisfaccionModel.objects.filter(curso=curso_id,encuesta_id=encuesta_id).values('pregunta','curso_id').annotate(promedio=Avg('respuesta_valor')).exclude(pregunta__in=excluir)
                                                                                                    


def obtenerPromedioTotalEncuesta(encuesta_id,tipo,fecha_desde,fecha_hasta,excluir):
    if tipo == 'alumno':
        return respuestaAlumnoModel.objects.filter(encuesta_alumno_id=encuesta_id,
                                                                    curso__fecha_inicio__range=[fecha_desde,fecha_hasta],
                                                                    curso__fecha_termino__range=[fecha_desde,fecha_hasta]).values('pregunta').annotate(promedio=Avg('respuesta_valor')).exclude(pregunta__in=excluir)
    
    if tipo == 'satisfaccion':
        return respuestaSatisfaccionModel.objects.filter(encuesta_id=encuesta_id,
                                                                    curso__fecha_inicio__range=[fecha_desde,fecha_hasta],
                                                                    curso__fecha_termino__range=[fecha_desde,fecha_hasta]).values('pregunta').annotate(promedio=Avg('respuesta_valor')).exclude(pregunta__in=excluir)
    if tipo == 'recepcion_servicio':
        return respuestaRecepcionServicioModel.objects.filter(encuesta_recepcion_id=encuesta_id,
                                                                    curso__fecha_inicio__range=[fecha_desde,fecha_hasta],
                                                                    curso__fecha_termino__range=[fecha_desde,fecha_hasta]).values('pregunta').annotate(promedio=Avg('respuesta_valor')).exclude(pregunta__in=excluir)