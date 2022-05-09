from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from encuestas.models.preguntaAlumnoModel import preguntaAlumnoModel
from encuestas.models.alumnoCursoModel import alumnoCursoModel
from encuestas.models.alumnoModel import alumnoModel
from encuestas.models.encuestaAlumnoModel import encuestaAlumnoModel
from encuestas.models.respuestaAlumnoModel import respuestaAlumnoModel

from encuestas.views.utils.utils import generarError, guardarRespuestaEncuestaCurso, validarRespuestaEncuesta


def encuesta_curso_view(request,encuesta_id):
    try:
        encuesta_existe = encuestaAlumnoModel.objects.filter(enc_curso_id=encuesta_id).exists()
        if not encuesta_existe:
            return redirect('home')
        try:
            current_user = request.user
            encuesta = encuestaAlumnoModel.objects.get(enc_curso_id=encuesta_id)
            alumno_curso = alumnoCursoModel.objects.get(al_cu_id=encuesta.alumno_curso_id)
            alumno = alumnoModel.objects.get(user_id=current_user.id)
            if not alumno_curso.alumno_id == alumno.alumno_id:
                data = {
                    'error': True,
                    'mensaje': 'El usuario actual no coincide con el de la encuesta, por favor contacte con el administrador.',
                    'status': 403
                }
                return render(request, 'error/error.html',data, status=403)       
        except:
            data = {
                'error': True,
                'mensaje': 'El usuario no coindice con el asociado a la encuesta',
                'status': 403,
            }
            return render(request, 'error/error.html',data, status=403)

        try:
            preguntas = preguntaAlumnoModel.objects.filter(encuesta_curso=encuesta_id)
        except:
            return HttpResponse(request,'ERROR AL TRAER PREGUNTAS')
        
        if preguntas.count == 0:
            data = {
                'error_preguntas': 'El alumno no tiene una encuesta asociada'
            }
            return render(request,'encuestas/encuesta_curso.html', data)

        lista_preguntas = []
        for item in preguntas:
            pregunta = {
                'pregunta' : item.pregunta,
                'respuesta':item.valor.split(','),
                'orden': item.orden
            }
            lista_preguntas.append(pregunta)
            
        data = {
            'encuesta': encuesta,
            'lista_preguntas':lista_preguntas
        }        

        try:
            if request.method == 'POST':
                valores_respuestas_m = [request.POST.get('respuesta1', False), request.POST.get('respuesta2', False), 
                                        request.POST.get('respuesta3', False), request.POST.get('respuesta4', False),
                                        request.POST.get('respuesta5', False), request.POST.get('respuesta6', False),
                                        request.POST.get('respuesta7', False), request.POST.get('respuesta8', False),
                                        request.POST.get('respuesta9', False), request.POST.get('respuesta10', False),
                                        request.POST.get('respuesta11', False), request.POST.get('respuesta12', False)]
                
                pregunta1 = preguntas.get(orden=1).pregunta
                pregunta2 = preguntas.get(orden=2).pregunta
                pregunta3 = preguntas.get(orden=3).pregunta
                pregunta4 = preguntas.get(orden=4).pregunta
                pregunta5 = preguntas.get(orden=5).pregunta
                pregunta6 = preguntas.get(orden=6).pregunta
                pregunta7 = preguntas.get(orden=7).pregunta
                pregunta8 = preguntas.get(orden=8).pregunta
                pregunta9 = preguntas.get(orden=9).pregunta
                pregunta10 = preguntas.get(orden=10).pregunta
                pregunta11 = preguntas.get(orden=11).pregunta
                pregunta12 = preguntas.get(orden=12).pregunta
                pregunta13 = preguntas.get(orden=13).pregunta

                respondida = respuestaAlumnoModel.objects.filter(encuesta_curso=encuesta_id).exists()
                if respondida:
                    return generarError(render,request,'La encuesta ya fue contestada',404)                    

                if(validarRespuestaEncuesta(valores_respuestas_m, 'M')):
                    guardarRespuestaEncuestaCurso(pregunta1, request.POST['respuesta1'], encuesta_id)
                    guardarRespuestaEncuestaCurso(pregunta2, request.POST['respuesta2'], encuesta_id)
                    guardarRespuestaEncuestaCurso(pregunta3, request.POST['respuesta3'], encuesta_id)
                    guardarRespuestaEncuestaCurso(pregunta4, request.POST['respuesta4'], encuesta_id)
                    guardarRespuestaEncuestaCurso(pregunta5, request.POST['respuesta5'], encuesta_id)
                    guardarRespuestaEncuestaCurso(pregunta6, request.POST['respuesta6'], encuesta_id)
                    guardarRespuestaEncuestaCurso(pregunta7, request.POST['respuesta7'], encuesta_id)
                    guardarRespuestaEncuestaCurso(pregunta8, request.POST['respuesta8'], encuesta_id)
                    guardarRespuestaEncuestaCurso(pregunta9, request.POST['respuesta9'], encuesta_id)
                    guardarRespuestaEncuestaCurso(pregunta10, request.POST['respuesta10'], encuesta_id)
                    guardarRespuestaEncuestaCurso(pregunta11, request.POST['respuesta11'], encuesta_id)
                    guardarRespuestaEncuestaCurso(pregunta12, request.POST['respuesta12'], encuesta_id)
                    guardarRespuestaEncuestaCurso(pregunta13, request.POST['respuesta13'], encuesta_id)
                    
                    messages.success(request,'La encuesta fue guardada satisfactoriamente')
                    return redirect(to='home')
                else:
                    return generarError(render,request,'No se validaron las respuestas en el servidor',400)

        except:
            return generarError(render,request,'No se guardaron las respuestas',400)
            # data = {
            #     'error': True,
            #     'mensaje': 'No se guardaron las respuestas',
            #     'status': 400
            # }
            # return render(request, 'error/error.html',data, status=400)        
        
        return render(request, 'encuestas/encuesta_curso.html', data)
    
    except:
        return generarError(render,request,'No se cargaron los datos de la encuesta, por favor contacte al administrador',400)
        # data = {
        #     'error': True,
        #     'mensaje': 'No se cargaron los datos de la encuesta, por favor contacte al administrador',
        #     'status': 400
        # }
        # return render(request, 'error/error.html',data, status=400)        
