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

from encuestas.views.utils.utils import generarError, guardarRespuestaEncuestaSatisfaccion, obtenerValorRespuesta, validarRespuestaEncuesta

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
            data = {
                'error_preguntas': 'El curso no tiene una encuesta asociada'
            }
            return render(request,'encuestas/encuesta_recepcion_servicio.html', data)
        
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
        
        return render(request, 'encuestas/encuesta_recepcion_servicio.html', data)
    except:        
        return generarError(render,request,'No se cargaron los datos de la encuesta, por favor contacte al administrador',404)    
