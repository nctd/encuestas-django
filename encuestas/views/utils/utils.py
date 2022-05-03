from msilib.schema import Error
from encuestas.models import cursoModel
from ...forms import PreguntaCursoForm, RespuestaSatisfaccionForm

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


def guardarRespuestaEncuestaSatisfaccion(pregunta, respuesta, encuesta, curso):
    data_resp = {
        'pregunta': pregunta,
        'respuesta': respuesta,
        'encuesta': encuesta,
        'curso': curso
    }
    respuesta = RespuestaSatisfaccionForm(data=data_resp)
    if respuesta.is_valid():
        respuesta.save()

def validarCurso(curso_id,nombre_curso):
    exists = cursoModel.objects.filter(curso_id=curso_id,nombre_curso=nombre_curso).exists()
    if exists: 
        return True 
    return False

def guardarRespuestaEncuestaCurso(pregunta, respuesta, id_encuesta, alumno):
    data_preg = {
        'pregunta': pregunta,
        'respuesta': respuesta,
        'e_curso': id_encuesta,
        'alumno': alumno
    }
    pregunta = PreguntaCursoForm(data=data_preg)
    if pregunta.is_valid():
        pregunta.save()
    else:
        return Exception('ERROR')
