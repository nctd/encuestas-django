
from encuestas.models.cursoEncuestaSatisfaccionModel import cursoEncuestaSatisfaccionModel
from encuestas.models.cursoModel import cursoModel
from encuestas.models.encuestaSatisfaccionModel import encuestaSatisfaccionModel
from encuestas.models.preguntaSatisfaccionModel import preguntaSatisfaccionModel
from encuestas.models.respuestaSatisfaccionModel import respuestaSatisfaccionModel
from encuestas.views.utils.utils import obtenerPromedioEncuesta, obtenerPromedioTotalEncuesta


def obtenerResumenSatisfaccion(fecha_desde,fecha_hasta):
    encuestas_satisfaccion = encuestaSatisfaccionModel.objects.all()
    list_respuestas_satisfaccion = []
    list_encuestas_satisfaccion = []
    total_acumulado_satisfaccion = 0
    for encuesta in encuestas_satisfaccion:
        preguntas = preguntaSatisfaccionModel.objects.filter(encuesta_id=encuesta.encuesta_id).exclude(valor='Observacion').values_list('pregunta',flat=True)


        cursos = cursoEncuestaSatisfaccionModel.objects.filter(encuesta_id=encuesta.encuesta_id,
                                                                       curso__fecha_inicio__range=[fecha_desde,fecha_hasta],
                                                                       curso__fecha_termino__range=[fecha_desde,fecha_hasta])

        obs_preguntas = preguntaSatisfaccionModel.objects.filter(encuesta_id=encuesta.encuesta_id,valor='Observacion').values_list('pregunta',flat=True)
        preguntas_exclude = [a for a in obs_preguntas]

        respuestas = respuestaSatisfaccionModel.objects.filter(encuesta_id=encuesta.encuesta_id,
                                                                curso__fecha_inicio__range=[fecha_desde,fecha_hasta],
                                                                curso__fecha_termino__range=[fecha_desde,fecha_hasta]).exclude(pregunta__in=preguntas_exclude)
        


        list_cursos_satisfaccion = []
        # list_promedios_satisfaccion = []
        list_prom_acumulados_satisfaccion = []
        total_promedios_satisfaccion = []
        list_respuestas_satisfaccion = []
        for curso in cursos:
            curso = cursoModel.objects.get(curso_id=curso.curso_id)
            if respuestas.filter(curso_id=curso.curso_id).exists():
                list_cursos_satisfaccion.append(curso)
  
            
            for respuesta in respuestas.filter(curso_id=curso.curso_id):
                list_respuestas_satisfaccion.append(respuesta)
                
            if not list_respuestas_satisfaccion == [] and respuestas.filter(curso_id=curso.curso_id).exists():
 
                promedio_acumulado =  round(sum((value['promedio']) 
                                                for value in obtenerPromedioEncuesta(encuesta.encuesta_id,curso.curso_id,'satisfaccion',preguntas_exclude))/preguntas.count(),1)
                # print(promedio_acumulado)
                list_prom_acumulados_satisfaccion.append({
                    'valor': promedio_acumulado,
                    'curso_id': curso.curso_id
                })


                # for value in obtenerPromedioEncuesta(encuesta.encuesta_id,curso.curso_id,'satisfaccion'):
                #     list_promedios_satisfaccion.append(value)

            
                total_promedios_satisfaccion = obtenerPromedioTotalEncuesta(encuesta.encuesta_id,'satisfaccion',fecha_desde,fecha_hasta,preguntas_exclude)

                total_acumulado_satisfaccion = round(sum(prom['valor'] for prom in list_prom_acumulados_satisfaccion)/len(list_prom_acumulados_satisfaccion),1)
                
                # print(total_acumulado_satisfaccion)

        data_table = {
            'encuesta': encuesta,
            'preguntas':preguntas,
            'respuestas': list_respuestas_satisfaccion,
            'cursos':list_cursos_satisfaccion,
            # 'promedios':list_promedios_satisfaccion,
            'acumulados':list_prom_acumulados_satisfaccion,
            'total_promedios': total_promedios_satisfaccion,
            'total_acumulado': total_acumulado_satisfaccion
        }
        if not respuestas.count() >= preguntas.count() and not preguntas.count() > 0:
            data_table = {}
            # list_encuestas_satisfaccion = []
            list_encuestas_satisfaccion.append(data_table)
            # return list_encuestas_satisfaccion
        list_encuestas_satisfaccion.append(data_table)
    return list_encuestas_satisfaccion