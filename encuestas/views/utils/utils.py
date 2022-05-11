from django.contrib import messages

from encuestas.models import cursoModel
from ...forms import RespuestaAlumnoForm, RespuestaSatisfaccionForm

def validarRespuestaEncuesta(valor, respuesta):
    posibles_respuestas = valor.split(',')
    if 'Observacion' in posibles_respuestas:
        return True
    if (respuesta in posibles_respuestas):
        return True
    return False
    # if(type_value == 'M'):
    #     for val in value:
    #         if(val not in ['Deficiente', 'Malo', 'Regular', 'Bueno', 'Excelente']):
    #             return False
    #     else:
    #         return True
    # if(type_value == 'SN'):
    #     for val in value:
    #         if(val not in ['Si', 'No']):
    #             return False
    #     else:
    #         return True
    # return False


def guardarRespuestaEncuestaSatisfaccion(data,encuesta,curso):
    print(data['respuesta_texto'])
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

def guardarRespuestaEncuestaCurso(pregunta, respuesta, encuesta_id):
    try:
        data_resp = {
            'pregunta': pregunta,
            'respuesta': respuesta,
            'encuesta_curso': encuesta_id,
        }

        respuesta = RespuestaAlumnoForm(data=data_resp)
        if respuesta.is_valid():
            respuesta.save()
    except:
        raise
    
    
def generarError(render,request,mensaje,status):
    data = {
        'error': True,
        'mensaje': mensaje,
        'status': status
    }
    return render(request, 'error/error.html',data, status=status)       

def obtenerValorRespuesta(respuesta):
    valor = 0
    if(respuesta in ['Deficiente', 'Malo', 'Regular', 'Bueno', 'Excelente', 'Si','No']):
        if respuesta == 'Deficiente': valor = 1
        if respuesta == 'Malo': valor = 2
        if respuesta == 'Regular': valor = 3
        if respuesta == 'Bueno': valor = 4
        if respuesta == 'Excelente': valor = 5
        if respuesta == 'Si': valor = 1
        if respuesta == 'No': valor = 0
    return valor 

