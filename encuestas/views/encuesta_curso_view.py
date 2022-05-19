from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import transaction

from encuestas.models.cursoEncuestaAlumnoModel import cursoEncuestaAlumnoModel
from encuestas.models.cursoModel import cursoModel
from encuestas.models.preguntaAlumnoModel import preguntaAlumnoModel
from encuestas.models.alumnoCursoModel import alumnoCursoModel
from encuestas.models.alumnoModel import alumnoModel
from encuestas.models.encuestaAlumnoModel import encuestaAlumnoModel
from encuestas.models.respuestaAlumnoModel import respuestaAlumnoModel

from encuestas.views.utils.utils import generarError, guardarRespuestaEncuestaAlumno, obtenerValorRespuesta, validarRespuestaEncuesta


@login_required(login_url='/auth/login_user')
def encuesta_curso_view(request,encuesta_id,curso_id):
    try:
        encuesta_existe = encuestaAlumnoModel.objects.filter(encuesta_alumno_id=encuesta_id).exists()
        if not encuesta_existe:
            return redirect('home')
        try:
            current_user = request.user
            alumno = alumnoModel.objects.get(user_id=current_user.id)
            curso = cursoModel.objects.get(curso_id=curso_id)
            print(curso.empresa.nombre_empresa)
            curso_encuesta = cursoEncuestaAlumnoModel.objects.get(curso_id=curso_id,encuesta_id=encuesta_id)
            alumno_curso = alumnoCursoModel.objects.get(alumno_id=alumno.alumno_id,curso_id=curso_id)
            encuesta = encuestaAlumnoModel.objects.get(encuesta_alumno_id=encuesta_id)
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

        respuesta_existe = respuestaAlumnoModel.objects.filter(encuesta_alumno=encuesta.encuesta_alumno_id,alumno_curso=alumno_curso.alumno_curso_id ).exists()
        if respuesta_existe:
            messages.info(request,'La encuesta ya fue enviada')
            return redirect(to='home')
        try:
            preguntas = preguntaAlumnoModel.objects.filter(encuesta_curso=encuesta.encuesta_alumno_id)
            print(preguntas.count())
        except:
            return generarError(render,request,'No se encontraron preguntas asociadas a la encuesta',404)        
            # return HttpResponse(request,'ERROR AL TRAER PREGUNTAS')
        
        # BORRAR PROB
        if preguntas.count() == 0:
            return generarError(render,request,'La encuesta no tiene preguntas asociadas',404)   

        lista_preguntas = []
        for item in preguntas:
            pregunta = {
                'pregunta' : item.pregunta,
                'respuesta':item.valor.split(','),
                'orden': item.orden
            }
            lista_preguntas.append(pregunta)
            
        data = {
            'curso':curso,
            'encuesta': encuesta,
            'lista_preguntas':lista_preguntas
        }        

        try:
            if request.method == 'POST':
                lista_respuestas = []
                for value in request.POST:
                    if value.startswith('respuesta'):
                        orden_respuesta = value.split('respuesta')[1]
                        pregunta_resp = preguntas.get(orden=orden_respuesta)
                        
                        respuesta_texto = request.POST.get(value,False)
                        if (respuesta_texto == ''):
                            respuesta_texto = 'NC'
                            
                        data_respuesta = {
                            'respuesta_texto': respuesta_texto,
                            'orden_respuesta': orden_respuesta,
                            'valores_respuesta': pregunta_resp.valor,
                            'pregunta':pregunta_resp.pregunta,
                            'respuesta_valor': obtenerValorRespuesta(request.POST.get(value,False))
                        }
                        lista_respuestas.append(data_respuesta)

                if len(lista_respuestas) != preguntas.count():
                    
                    return generarError(render,request,'No se guardaron las respuestas',500)
                
                with transaction.atomic():      
                    for value in lista_respuestas:
                        if validarRespuestaEncuesta(value['valores_respuesta'],value['respuesta_texto']):
                            guardarRespuestaEncuestaAlumno(value,encuesta.encuesta_alumno_id,alumno_curso.alumno_curso_id)
                        else:
                            return generarError(render,request,'No se validaron las respuestas en el servidor',500)        
                    
                messages.success(request,'La encuesta fue guardada satisfactoriamente')
                return redirect(to='home')                                    

        except:
            return generarError(render,request,'No se guardaron las respuestas',400)
        
        return render(request, 'encuestas/encuesta_curso.html', data)
    
    except:
        return generarError(render,request,'No se cargaron los datos de la encuesta, por favor contacte al administrador',404)

