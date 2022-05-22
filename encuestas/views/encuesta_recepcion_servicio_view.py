from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import transaction

from encuestas.models.cursoEncuestaRecepcionServicioModel import cursoEncuestaRecepcionServicioModel
from encuestas.models.cursoModel import cursoModel
from encuestas.models.empresaModel import empresaModel
from encuestas.models.encuestaRecepcionServicio import encuestaRecepcionServicioModel
from encuestas.models.preguntaRecepcionServicio import preguntaRecepcionServicioModel
from encuestas.models.respuestaRecepcionServicioModel import respuestaRecepcionServicioModel

from encuestas.views.utils.utils import generarError, guardarRespuestaEncuestaRecepcionServicio, guardarRespuestaEncuestaSatisfaccion, obtenerResultadoRecepcionServicio, obtenerValorRespuesta, validarRespuestaEncuesta

@login_required(login_url='/auth/login_user')
def encuesta_recepcion_servicio_view(request,encuesta_id,curso_id):
    try:
        encuesta_existe = encuestaRecepcionServicioModel.objects.filter(encuesta_recepcion_id=encuesta_id).exists()
        if not encuesta_existe:
            return render(request,'home')
        try:
            current_user = request.user
            empresa = empresaModel.objects.get(user=current_user.id)
            curso = cursoModel.objects.get(curso_id=curso_id)         
            curso_recepcion = cursoEncuestaRecepcionServicioModel.objects.get(curso_id=curso_id,encuesta_recepcion_id=encuesta_id)
            encuesta = encuestaRecepcionServicioModel.objects.get(encuesta_recepcion_id=encuesta_id)
        except:
            return generarError(render,request,'El curso no coindice con el asociado a la encuesta',403)
                
        respuesta_existe = respuestaRecepcionServicioModel.objects.filter(encuesta_recepcion_id=encuesta.encuesta_recepcion_id,curso=curso.curso_id).exists()
        if respuesta_existe:
            messages.info(request,'La encuesta ya fue enviada')
            return redirect(to='home')
        
        try:
            preguntas = preguntaRecepcionServicioModel.objects.filter(encuesta_recepcion_id=encuesta.encuesta_recepcion_id)
        except:
            return generarError(render,request,'No se encontraron preguntas asociadas a la encuesta',404)   
        
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
            'curso': curso,
            'encuesta':encuesta,
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
                            'respuesta_valor': obtenerValorRespuesta(request.POST.get(value,False)),
                            'porcentaje': pregunta_resp.porcentaje
                        }
                        lista_respuestas.append(data_respuesta)
                        
                if len(lista_respuestas) != preguntas.count():
                    return generarError(render,request,'No se guardaron las respuestas',500)       
                
                with transaction.atomic():                
                    for value in lista_respuestas:
                        if validarRespuestaEncuesta(value['valores_respuesta'],value['respuesta_texto']):
                            guardarRespuestaEncuestaRecepcionServicio(value,encuesta.encuesta_recepcion_id,curso.curso_id)
                        else:
                            return generarError(render,request,'No se validaron las respuestas en el servidor',500)
                    
                messages.success(request,'La encuesta fue guardada satisfactoriamente')
                return redirect(to='home')           
                                  
        except:
            return generarError(render,request,'No se guardaron las respuestas',400)  
                    
        return render(request, 'encuestas/encuesta_recepcion_servicio.html', data)
    
    except:        
        return generarError(render,request,'No se cargaron los datos de la encuesta, por favor contacte al administrador',404)    