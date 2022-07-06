from encuestas.models.cursoEncuestaAlumnoModel import cursoEncuestaAlumnoModel
from encuestas.models.cursoModel import cursoModel
from encuestas.models.encuestaAlumnoModel import encuestaAlumnoModel
from encuestas.models.preguntaAlumnoModel import preguntaAlumnoModel
from encuestas.models.respuestaAlumnoModel import respuestaAlumnoModel
from encuestas.views.utils.utils import obtenerPromedioEncuesta, obtenerPromedioTotalEncuesta


def obtenerResumenAlumnos(fecha_desde,fecha_hasta):
    encuestas_alumno = encuestaAlumnoModel.objects.all()
    list_encuestas_alumno = []
    total_acumulado = 0
    for encuesta in encuestas_alumno:
        preguntas = preguntaAlumnoModel.objects.filter(encuesta_alumno_id=encuesta.encuesta_alumno_id).exclude(valor='Observacion').values_list('pregunta',flat=True)
        cursos = cursoEncuestaAlumnoModel.objects.filter(encuesta_id=encuesta.encuesta_alumno_id,
                                                            curso__fecha_inicio__range=[fecha_desde,fecha_hasta],
                                                            curso__fecha_termino__range=[fecha_desde,fecha_hasta])
        
        
        obs_preguntas = preguntaAlumnoModel.objects.filter(encuesta_alumno_id=encuesta.encuesta_alumno_id,valor='Observacion').values_list('pregunta',flat=True)
        preguntas_exclude = [a for a in obs_preguntas]
        
        respuestas = respuestaAlumnoModel.objects.filter(encuesta_alumno_id=encuesta.encuesta_alumno_id,
                                                        curso__fecha_inicio__range=[fecha_desde,fecha_hasta],
                                                        curso__fecha_termino__range=[fecha_desde,fecha_hasta]).exclude(pregunta__in=preguntas_exclude)
        

        list_cursos = []
        list_promedios = []
        list_prom_acumulados = []
        total_promedios = []
        for curso in cursos:
            curso = cursoModel.objects.get(curso_id=curso.curso_id)
            if respuestas.filter(curso_id=curso.curso_id).exists():
                list_cursos.append(curso)
            
            if respuestas.filter(curso_id=curso.curso_id).exists():
                promedio_acumulado =  round(sum((value['promedio']) 
                                                for value in obtenerPromedioEncuesta(encuesta.encuesta_alumno_id,curso.curso_id,'alumno',preguntas_exclude))/preguntas.count(),1)
                
                list_prom_acumulados.append({
                    'valor': promedio_acumulado,
                    'curso_id': curso.curso_id
                })

            
                for value in obtenerPromedioEncuesta(encuesta.encuesta_alumno_id,curso.curso_id,'alumno',preguntas_exclude):
                    list_promedios.append(value)
                
                total_acumulado = round(sum(prom['valor'] for prom in list_prom_acumulados)/len(list_prom_acumulados),2)


 
    
            preguntas_promedios = {d['pregunta'] for d in list_promedios}
            # cursos_promedios= {d['curso_id'] for d in list_promedios}
            total_promedios = ([{'pregunta':pregunta, 'total': sum(d['promedio'] /cursos.count()
                                            for d in list_promedios if d['pregunta']==pregunta)} for pregunta in preguntas_promedios])

        data_table = {
            'encuesta': encuesta,
            'preguntas':preguntas,
            'cursos':list_cursos,
            'promedios':list_promedios,
            'acumulados':list_prom_acumulados,
            'total_promedios': total_promedios,
            'total_acumulado': total_acumulado
        }
        if not respuestas.count() >= preguntas.count() and not preguntas.count() > 0:
            data_table = {}
            list_encuestas_alumno.append(data_table)
        list_encuestas_alumno.append(data_table)
    return list_encuestas_alumno