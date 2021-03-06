from encuestas.models.cursoEncuestaRecepcionServicioModel import cursoEncuestaRecepcionServicioModel
from encuestas.models.cursoModel import cursoModel
from encuestas.models.encuestaRecepcionServicio import encuestaRecepcionServicioModel
from encuestas.models.preguntaRecepcionServicio import preguntaRecepcionServicioModel
from encuestas.models.respuestaRecepcionServicioModel import respuestaRecepcionServicioModel
from encuestas.views.utils.utils import obtenerPromedioTotalEncuesta, obtenerResultadoRecepcionServicio


def obtenerResumenRecepcionServicio(fecha_desde,fecha_hasta):
    encuestas_recepcion = encuestaRecepcionServicioModel.objects.all()
    list_encuestas_recepcion = []
    for value in encuestas_recepcion:
        preguntas = preguntaRecepcionServicioModel.objects.filter(encuesta_recepcion_id=value.encuesta_recepcion_id).exclude(valor='Observacion').values_list('pregunta',flat=True)
        cursos = cursoEncuestaRecepcionServicioModel.objects.filter(encuesta_recepcion_id=value.encuesta_recepcion_id,
                                                                    curso__fecha_inicio__range=[fecha_desde,fecha_hasta],
                                                                    curso__fecha_termino__range=[fecha_desde,fecha_hasta])
        
        
        obs_preguntas = preguntaRecepcionServicioModel.objects.filter(encuesta_recepcion_id=value.encuesta_recepcion_id).exclude(valor='Observacion').values_list('pregunta',flat=True)
        preguntas_exclude = [a for a in obs_preguntas]
        
        respuestas = respuestaRecepcionServicioModel.objects.filter(encuesta_recepcion_id=value.encuesta_recepcion_id,
                                                                    curso__fecha_inicio__range=[fecha_desde,fecha_hasta],
                                                                    curso__fecha_termino__range=[fecha_desde,fecha_hasta]).exclude(pregunta__in=preguntas_exclude)

        list_cursos = []
        list_porcentaje = []
        list_respuestas = []
        total_promedios_recepcion = []
        total_porcentaje = []
        for curso in cursos:
            curso = cursoModel.objects.get(curso_id=curso.curso_id)
            if respuestas.filter(curso_id=curso.curso_id).exists():
                list_cursos.append(curso)
            
            for respuesta in respuestas.filter(curso_id=curso.curso_id):
                list_respuestas.append(respuesta)
                
            if not list_respuestas == [] and respuestas.filter(curso_id=curso.curso_id).exists():
                data_porcentaje = {
                    'porc': obtenerResultadoRecepcionServicio(value.encuesta_recepcion_id,curso.curso_id),
                    'curso_id':curso.curso_id
                }
                list_porcentaje.append(data_porcentaje)
                
                total_promedios_recepcion = obtenerPromedioTotalEncuesta(value.encuesta_recepcion_id,'recepcion_servicio',fecha_desde,fecha_hasta,preguntas_exclude)
                total_porcentaje = round(sum(porc['porc'] for porc in list_porcentaje)/len(list_porcentaje),1)


        data_table = {
            'encuesta':value,
            'preguntas':preguntas,
            'cursos':list_cursos,
            'respuestas':list_respuestas,
            'porcentajes':list_porcentaje,
            'promedio_puntaje':total_promedios_recepcion,
            'total_porcentaje':total_porcentaje
        }
        if not respuestas.count() >= preguntas.count() and not preguntas.count() > 0:
            data_table = {}
            list_encuestas_recepcion.append(data_table)
            
        list_encuestas_recepcion.append(data_table)
    return list_encuestas_recepcion