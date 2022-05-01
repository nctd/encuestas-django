from ...forms import PreguntaSatisfaccionForm

def validarRespuestaSatisfaccion(value, type_value):
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


def guardarRespuestaEncuesta(pregunta, respuesta, id_encuesta):
    data_preg = {
        'pregunta': pregunta,
        'respuesta': respuesta,
        'e': id_encuesta
    }
    pregunta = PreguntaSatisfaccionForm(data=data_preg)
    if pregunta.is_valid():
        pregunta.save()
