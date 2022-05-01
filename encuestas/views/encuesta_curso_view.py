from django.shortcuts import render
from django.contrib import messages

from encuestas.views.utils.utils import guardarRespuestaEncuesta, validarRespuestaSatisfaccion

from ..forms import EncuestaSatisfaccionForm


pregunta_1 = 'Se cumplieron los objetivos del curso '
pregunta_2 = 'El contenido del curso fue interesante e importante para su trabajo'
pregunta_3 = 'Intercambio de experiencias entre los participantes '
pregunta_4 = 'Dinámica del curso'
pregunta_5 = 'Ambiente de Trabajo'
pregunta_6 = 'Comunicación y dominio de los contenidos por parte del Relator'
pregunta_7 = 'Puntualidad del Relator'
pregunta_8 = 'Calidad de su manual de trabajo'
pregunta_9 = 'Proyección de la Clase (Contenidos, nitidez, colores)'
pregunta_10 = 'Que le pareció el trato que recibió como cliente'
pregunta_11 = 'Instalaciones (Infraestructura)'
pregunta_12 = 'Servicio de Alimentación.'


def encuesta_curso_view(request):
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
        'pregunta_10': pregunta_10,
        'pregunta_11': pregunta_11,
        'pregunta_12': pregunta_12,
        'respuestas': ['Deficiente', 'Malo', 'Regular', 'Bueno', 'Excelente'],
    }
    if request.method == 'POST':
        valores_respuestas_m = [request.POST.get('respuesta1', False), request.POST.get('respuesta2', False), 
                                request.POST.get('respuesta3', False), request.POST.get('respuesta4', False)]
        valores_respuestas_sn = [request.POST.get('respuesta5', False), request.POST.get('respuesta6', False),
                                 request.POST.get('respuesta7', False), request.POST.get('respuesta8', False)]

        if(validarRespuestaSatisfaccion(valores_respuestas_m, 'M') and validarRespuestaSatisfaccion(valores_respuestas_sn, 'SN')):
            encuesta = EncuestaSatisfaccionForm(data=True)
            if(encuesta.is_valid()):
                e_id = encuesta.save()
                guardarRespuestaEncuesta(pregunta_1, request.POST['respuesta1'], e_id)
                guardarRespuestaEncuesta(pregunta_2, request.POST['respuesta2'], e_id)
                guardarRespuestaEncuesta(pregunta_3, request.POST['respuesta3'], e_id)
                guardarRespuestaEncuesta(pregunta_4, request.POST['respuesta4'], e_id)
                guardarRespuestaEncuesta(pregunta_5, request.POST['respuesta5'], e_id)
                guardarRespuestaEncuesta(pregunta_6, request.POST['respuesta6'], e_id)
                guardarRespuestaEncuesta(pregunta_7, request.POST['respuesta7'], e_id)
                guardarRespuestaEncuesta(pregunta_8, request.POST['respuesta8'], e_id)
                guardarRespuestaEncuesta(pregunta_9, request.POST['respuesta9'], e_id)
        else:
            print('not post')
            data['error'] = True
            return render(request,'encuestas/encuesta_curso.html', data)

    else:
        print('nopost')
    return render(request, 'encuestas/encuesta_curso.html', data)

