from django.shortcuts import render
from django.contrib import messages

from ..forms import EncuestaSatisfaccionForm

from encuestas.views.utils.utils import guardarRespuestaEncuestaSatisfaccion, validarRespuestaEncuesta

pregunta_1 = '¿Cómo fue la atención general que se le brindó?'
pregunta_2 = '¿Se demostró conocimiento del o los servicios ofrecidos?'
pregunta_3 = '¿La persona administrativa, contestó de forma rápida y adecuada sus inquietudes?'
pregunta_4 = '¿Qué le pareció el servicio en general brindado?'
pregunta_5 = '¿Recomendaría al organismo de capacitación?'
pregunta_6 = '¿Compraría otro servicio al organismo?'
pregunta_7 = '¿El servicio prestado, cumplió con sus expectativas?'
pregunta_8 = '¿Se cumplió con lo planificado en el Servicio?'
pregunta_9 = '¿Qué otros cursos le gustarían tomar?'


def encuesta_satisfaccion_view(request):
    data = {
        'pregunta_1': pregunta_1,
        'pregunta_2': pregunta_2,
        'pregunta_3': pregunta_3,
        'pregunta_4': pregunta_4,
        'pregunta_5': pregunta_5,
        'pregunta_6': pregunta_6,
        'pregunta_7': pregunta_7,
        'pregunta_8': pregunta_8,
        'pregunta_9': pregunta_9,
        'respuestas': ['Deficiente', 'Malo', 'Regular', 'Bueno', 'Excelente'],
        'respuestas_2': ['Si', 'No']
    }
    if request.method == 'POST':
        valores_respuestas_m = [request.POST.get('respuesta1', False), request.POST.get('respuesta2', False), 
                                request.POST.get('respuesta3', False), request.POST.get('respuesta4', False)]
        valores_respuestas_sn = [request.POST.get('respuesta5', False), request.POST.get('respuesta6', False),
                                 request.POST.get('respuesta7', False), request.POST.get('respuesta8', False)]

        if(validarRespuestaEncuesta(valores_respuestas_m, 'M') and validarRespuestaEncuesta(valores_respuestas_sn, 'SN')):
            encuesta = EncuestaSatisfaccionForm(data=True)
            if(encuesta.is_valid()):
                e_id = encuesta.save()
                guardarRespuestaEncuestaSatisfaccion(pregunta_1, request.POST['respuesta1'], e_id)
                guardarRespuestaEncuestaSatisfaccion(pregunta_2, request.POST['respuesta2'], e_id)
                guardarRespuestaEncuestaSatisfaccion(pregunta_3, request.POST['respuesta3'], e_id)
                guardarRespuestaEncuestaSatisfaccion(pregunta_4, request.POST['respuesta4'], e_id)
                guardarRespuestaEncuestaSatisfaccion(pregunta_5, request.POST['respuesta5'], e_id)
                guardarRespuestaEncuestaSatisfaccion(pregunta_6, request.POST['respuesta6'], e_id)
                guardarRespuestaEncuestaSatisfaccion(pregunta_7, request.POST['respuesta7'], e_id)
                guardarRespuestaEncuestaSatisfaccion(pregunta_8, request.POST['respuesta8'], e_id)
                guardarRespuestaEncuestaSatisfaccion(pregunta_9, request.POST['respuesta9'], e_id)
        else:
            print('not post')
            data['error'] = True
            return render(request,'encuestas/encuesta_satisfaccion.html', data)

    else:
        print('nopost')
    return render(request, 'encuestas/encuesta_satisfaccion.html', data)

