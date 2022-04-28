import datetime
from django.shortcuts import render

from ..forms import EncuestaSatisfaccionForm, PreguntaSatisfaccionForm

pregunta_1 = '¿Cómo fue la atención general que se le brindó?'
pregunta_2 = '¿Se demostró conocimiento del o los servicios ofrecidos?'
pregunta_3 = '¿La persona administrativa, contestó de forma rápida y adecuada sus inquietudes?'
pregunta_4 = '¿Qué le pareció el servicio en general brindado?'
pregunta_5 = '¿Recomendaría al organismo de capacitación?'
pregunta_6 = '¿Compraría otro servicio al organismo?'
pregunta_7 = '¿El servicio prestado, cumplió con sus expectativas?'
pregunta_8 = '¿Se cumplió con lo planificado en el Servicio?'
pregunta_9 = 'Observaciones'

def encuesta_satisfaccion_view(request):
    data = {
        'pregunta_1' : pregunta_1,
        'respuestas': ['Deficiente','Malo','Regular','Bueno','Excelente']
    }
    if request.method == 'POST':
        valores_respuestas_m = [request.POST['respuesta1'],request.POST['respuesta2'],request.POST['respuesta3'],request.POST['respuesta4']]
        valores_respuestas_sn = [request.POST['respuesta5'],request.POST['respuesta6'],request.POST['respuesta7'],request.POST['respuesta8']]
        
        if(validarRespuestaSatisfaccion(valores_respuestas_m,'M') and validarRespuestaSatisfaccion(valores_respuestas_sn,'SN')):
            encuesta = EncuestaSatisfaccionForm(data=True)
            if(encuesta.is_valid()):
                e_id = encuesta.save()
                guardarRespuestaEncuesta(pregunta_1,request.POST['respuesta1'],e_id)
                guardarRespuestaEncuesta(pregunta_2,request.POST['respuesta2'],e_id)
                guardarRespuestaEncuesta(pregunta_3,request.POST['respuesta3'],e_id)
                guardarRespuestaEncuesta(pregunta_4,request.POST['respuesta4'],e_id)
                guardarRespuestaEncuesta(pregunta_5,request.POST['respuesta5'],e_id)
                guardarRespuestaEncuesta(pregunta_6,request.POST['respuesta6'],e_id)
                guardarRespuestaEncuesta(pregunta_7,request.POST['respuesta7'],e_id)
                guardarRespuestaEncuesta(pregunta_8,request.POST['respuesta8'],e_id)
        else:
            print('valor modificado por html ERROR')
            
        # print(request.POST['respuesta2'])
        

    else:
        print('nopost')
    return render(request, 'index.html',data)
    # return render(request, 'index.html')

def validarRespuestaSatisfaccion(value,type_value):
    if(type_value == 'M'):
        for val in value:
            if(val not in ['Deficiente','Malo','Regular','Bueno','Excelente']):
                return False
        else:
            return True
    if(type_value == 'SN'):
        for val in value:
            if(val not in ['Si','No']):
                return False
        else:
            return True
    return False

def guardarRespuestaEncuesta(pregunta,respuesta,id_encuesta):
    data_preg = {
        'pregunta':pregunta,
        'respuesta':respuesta,
        'e':id_encuesta
    }
    print(data_preg)
    pregunta = PreguntaSatisfaccionForm(data=data_preg)
    if pregunta.is_valid():
        pregunta.save()