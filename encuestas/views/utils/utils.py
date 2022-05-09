from django.contrib import messages

from encuestas.models import cursoModel
from ...forms import RespuestaCursoForm, RespuestaSatisfaccionForm

def validarRespuestaEncuesta(value, type_value):
    if(type_value == 'M'):
        for val in value:
            if(val not in ['Deficiente', 'Malo', 'Regular', 'Bueno', 'Excelente']):
                return False
        else:
            return True
    if(type_value == 'SN'):
        for val in value:
            if(val not in ['Si', 'No']):
                return False
        else:
            return True
    return False


def guardarRespuestaEncuestaSatisfaccion(pregunta, respuesta, encuesta):
    data_resp = {
        'pregunta': pregunta,
        'respuesta': respuesta,
        'encuesta': encuesta,
    }
    print(data_resp)
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
        data_preg = {
            'pregunta': pregunta,
            'respuesta': respuesta,
            'encuesta_curso': encuesta_id,
        }

        pregunta = RespuestaCursoForm(data=data_preg)
        if pregunta.is_valid():
            pregunta.save()
    except:
        raise
    
    
def generarError(render,request,mensaje,status):
    data = {
        'error': True,
        'mensaje': mensaje,
        'status': status
    }
    return render(request, 'error/error.html',data, status=status)       
