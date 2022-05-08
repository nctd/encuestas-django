from urllib import response
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from encuestas.models.cursoModel import cursoModel
from encuestas.models.respuestaSatisfaccionModel import respuestaSatisfaccionModel
from encuestas.models.empresaModel import empresaModel
from encuestas.models.encuestaSatisfaccionModel import encuestaSatisfaccionModel
from encuestas.models.preguntaSatisfaccionModel import preguntaSatisfaccionModel

from encuestas.views.utils.utils import guardarRespuestaEncuestaSatisfaccion, validarRespuestaEncuesta


@login_required(login_url='/auth/login_user')
def encuesta_satisfaccion_view(request,curso_id):
    # ESTA ENCUESTA, SOLO LA RESPONDEN LAS EMPRESAS
    try:
        print(curso_id)
        print('****************')
        current_user = request.user
        
        empresa_existe = empresaModel.objects.filter(user=current_user.id).exists()
        if not empresa_existe:
            # Exception('ERROR')
            return render(request,'home')
        
        empresa = empresaModel.objects.get(user=current_user.id)
        
        curso_existe = cursoModel.objects.filter(curso_id=curso_id).exists()
        if not curso_existe:
            # Exception('ERROR')
            return render(request,'home')
        
        curso = cursoModel.objects.get(curso_id=curso_id)
        
        encuesta_existe = encuestaSatisfaccionModel.objects.filter(curso=curso.curso_id).exists()

        if not encuesta_existe:
            # Exception('ERROR')
            return render(request,'home')
        
        encuesta = encuestaSatisfaccionModel.objects.get(curso=curso.curso_id)

        respuesta_existe = respuestaSatisfaccionModel.objects.filter(encuesta=encuesta.encuesta_id).exists()
        if respuesta_existe:
            messages.info(request,'La encuesta ya fue enviada')
            return redirect(to='home')
            # data = {
            #     'error': True,
            #     'mensaje': 'La encuesta ya fue contestada',
            #     'status': 400
            # }
            # return render(request, 'error/error.html',data, status=400)

        preguntas = preguntaSatisfaccionModel.objects.filter(encuesta=encuesta.encuesta_id)

        if preguntas.count == 0:
            data = {
                'error_preguntas': 'El curso no tiene una encuesta asociada'
            }
            return render(request,'encuestas/encuesta_satisfaccion.html', data)


        lista_preguntas = []
        for item in preguntas:
            pregunta = {
                'pregunta' : item.pregunta,
                'respuesta':item.valor.split(','),
                'orden': item.orden
            }
            lista_preguntas.append(pregunta)
        data = {
            'curso': curso,
            'lista_preguntas':lista_preguntas
        }
        print(data)
        try:
            if request.method == 'POST':
                valores_respuestas_m = [request.POST.get('respuesta1', False), request.POST.get('respuesta2', False), 
                                        request.POST.get('respuesta3', False), request.POST.get('respuesta4', False)]
                valores_respuestas_sn = [request.POST.get('respuesta5', False), request.POST.get('respuesta6', False),
                                        request.POST.get('respuesta7', False), request.POST.get('respuesta8', False)]
                
                pregunta1 = preguntas.get(orden=1).pregunta
                pregunta2 = preguntas.get(orden=2).pregunta
                pregunta3 = preguntas.get(orden=3).pregunta
                pregunta4 = preguntas.get(orden=4).pregunta
                pregunta5 = preguntas.get(orden=5).pregunta
                pregunta6 = preguntas.get(orden=6).pregunta
                pregunta7 = preguntas.get(orden=7).pregunta
                pregunta8 = preguntas.get(orden=8).pregunta
                pregunta9 = preguntas.get(orden=9).pregunta

                if(validarRespuestaEncuesta(valores_respuestas_m, 'M') and validarRespuestaEncuesta(valores_respuestas_sn, 'SN')):
                    guardarRespuestaEncuestaSatisfaccion(pregunta1, request.POST['respuesta1'], encuesta.encuesta_id,curso.curso_id)
                    guardarRespuestaEncuestaSatisfaccion(pregunta2, request.POST['respuesta2'], encuesta.encuesta_id,curso.curso_id)
                    guardarRespuestaEncuestaSatisfaccion(pregunta3, request.POST['respuesta3'], encuesta.encuesta_id,curso.curso_id)
                    guardarRespuestaEncuestaSatisfaccion(pregunta4, request.POST['respuesta4'], encuesta.encuesta_id,curso.curso_id)
                    guardarRespuestaEncuestaSatisfaccion(pregunta5, request.POST['respuesta5'], encuesta.encuesta_id,curso.curso_id)
                    guardarRespuestaEncuestaSatisfaccion(pregunta6, request.POST['respuesta6'], encuesta.encuesta_id,curso.curso_id)
                    guardarRespuestaEncuestaSatisfaccion(pregunta7, request.POST['respuesta7'], encuesta.encuesta_id,curso.curso_id)
                    guardarRespuestaEncuestaSatisfaccion(pregunta8, request.POST['respuesta8'], encuesta.encuesta_id,curso.curso_id)
                    guardarRespuestaEncuestaSatisfaccion(pregunta9, request.POST['respuesta9'], encuesta.encuesta_id,curso.curso_id)
                else:
                    data = {
                        'error': True,
                        'mensaje': 'No se validaron las respuestas en el servidor',
                        'status': 400
                    }
                    return render(request, 'error/error.html',data, status=400)
        except:
            data = {
                'error': True,
                'mensaje': 'No se guardaron las respuestas',
                'status': 400
            }
            return render(request, 'error/error.html',data, status=400)

        return render(request, 'encuestas/encuesta_satisfaccion.html', data)
    
    except:
        data = {
            'error': True,
            'mensaje': 'No se cargaron los datos de la encuesta, por favor contacte al administrador',
            'status': 400
        }
        return render(request, 'error/error.html',data, status=400)
