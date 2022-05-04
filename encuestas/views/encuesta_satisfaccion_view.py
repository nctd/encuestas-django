from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from encuestas.models import cursoModel
from encuestas.models.empresaModel import empresaModel

from encuestas.models.preguntaSatisfaccionModel import preguntaSatisfaccionModel

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

@login_required(login_url='/auth/login_user')
def encuesta_satisfaccion_view(request):
    # ESTA ENCUESTA, SOLO LA RESPONDEN LAS EMPRESAS
    try:
        current_user = request.user
        
        empresa_existe = empresaModel.objects.filter(user=current_user.id).exists()
        
        if empresa_existe:
            empresa = empresaModel.objects.get(user=current_user.id)
            curso_existe = cursoModel.objects.filter(resp_cliente=empresa.empresa_id).exists()
            if curso_existe:
                curso = cursoModel.objects.get(resp_cliente=empresa.empresa_id)
            else:  
                data = {
                    'curso': 'La empresa no tiene ningun curso asociado'
                }
                print(data)
                return render(request,'encuestas/encuesta_satisfaccion.html', data)
        else:
            print('no existe la empresa')
        preguntas = preguntaSatisfaccionModel.objects.all().values_list()
        
        data = {
            'pregunta_1': preguntas[0][1],
            'respuesta_1': preguntas[0][2].split(','),
            'pregunta_2': preguntas[1][1],
            'respuesta_2': preguntas[1][2].split(','),
            'pregunta_3': preguntas[2][1],
            'respuesta_3': preguntas[2][2].split(','),
            'pregunta_4': preguntas[3][1],
            'respuesta_4': preguntas[3][2].split(','),
            'pregunta_5': preguntas[4][1],
            'respuesta_5': preguntas[4][2].split(','),
            'pregunta_6': preguntas[5][1],
            'respuesta_6': preguntas[5][2].split(','),
            'pregunta_7': preguntas[6][1],
            'respuesta_7': preguntas[6][2].split(','),
            'pregunta_8': preguntas[7][1],
            'respuesta_8': preguntas[7][2].split(','),
            'pregunta_9': preguntas[8][1],
        }
        print(data)
        
        if request.method == 'POST':
            valores_respuestas_m = [request.POST.get('respuesta1', False), request.POST.get('respuesta2', False), 
                                    request.POST.get('respuesta3', False), request.POST.get('respuesta4', False)]
            valores_respuestas_sn = [request.POST.get('respuesta5', False), request.POST.get('respuesta6', False),
                                    request.POST.get('respuesta7', False), request.POST.get('respuesta8', False)]

            if(validarRespuestaEncuesta(valores_respuestas_m, 'M') and validarRespuestaEncuesta(valores_respuestas_sn, 'SN')):
                encuesta = EncuestaSatisfaccionForm(data=True)
                if(encuesta.is_valid()):
                    e_id = encuesta.save()
                    # guardarRespuestaEncuestaSatisfaccion(pregunta_1, request.POST['respuesta1'], e_id)
                    # guardarRespuestaEncuestaSatisfaccion(pregunta_2, request.POST['respuesta2'], e_id)
                    # guardarRespuestaEncuestaSatisfaccion(pregunta_3, request.POST['respuesta3'], e_id)
                    # guardarRespuestaEncuestaSatisfaccion(pregunta_4, request.POST['respuesta4'], e_id)
                    # guardarRespuestaEncuestaSatisfaccion(pregunta_5, request.POST['respuesta5'], e_id)
                    # guardarRespuestaEncuestaSatisfaccion(pregunta_6, request.POST['respuesta6'], e_id)
                    # guardarRespuestaEncuestaSatisfaccion(pregunta_7, request.POST['respuesta7'], e_id)
                    # guardarRespuestaEncuestaSatisfaccion(pregunta_8, request.POST['respuesta8'], e_id)
                    # guardarRespuestaEncuestaSatisfaccion(pregunta_9, request.POST['respuesta9'], e_id)
            else:
                print('not post')
                data['error'] = True
                return render(request,'encuestas/encuesta_satisfaccion.html', data)

        else:
            print('nopost')
        return render(request, 'encuestas/encuesta_satisfaccion.html', data)
    
    except:
        return render(request, 'encuestas/encuesta_satisfaccion.html')
