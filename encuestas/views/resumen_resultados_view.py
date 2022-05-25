from datetime import datetime
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Sum,Count,Avg
from encuestas.models.alumnoCursoModel import alumnoCursoModel

from encuestas.models.cursoEncuestaAlumnoModel import cursoEncuestaAlumnoModel
from encuestas.models.cursoEncuestaRecepcionServicioModel import cursoEncuestaRecepcionServicioModel
from encuestas.models.cursoEncuestaSatisfaccionModel import cursoEncuestaSatisfaccionModel
from encuestas.models.cursoModel import cursoModel
from encuestas.models.encuestaAlumnoModel import encuestaAlumnoModel
from encuestas.models.encuestaRecepcionServicio import encuestaRecepcionServicioModel
from encuestas.models.encuestaSatisfaccionModel import encuestaSatisfaccionModel
from encuestas.models.preguntaAlumnoModel import preguntaAlumnoModel
from encuestas.models.preguntaRecepcionServicio import preguntaRecepcionServicioModel
from encuestas.models.preguntaSatisfaccionModel import preguntaSatisfaccionModel
from encuestas.models.respuestaAlumnoModel import respuestaAlumnoModel

from encuestas.models.respuestaRecepcionServicioModel import respuestaRecepcionServicioModel
from encuestas.models.respuestaSatisfaccionModel import respuestaSatisfaccionModel
from encuestas.views.utils.utils import generarError, obtenerPromedioEncuesta, obtenerPromedioTotalEncuesta, obtenerResultadoRecepcionServicio

def resumen_resultados_view(request):
    current_user = request.user
    if not current_user.is_superuser:
        return redirect('home')
    data = {}
    if request.method == 'GET':

        if('fecha-desde' and 'fecha-hasta' in request.GET):
            fecha_desde = datetime.strptime(request.GET['fecha-desde'], "%d/%m/%Y").date()
            fecha_hasta = datetime.strptime(request.GET['fecha-hasta'], "%d/%m/%Y").date()
            encuestas_recepcion = encuestaRecepcionServicioModel.objects.all()
            print(fecha_desde,fecha_hasta)

            list_encuestas_recepcion = []
            for value in encuestas_recepcion:
                preguntas = preguntaRecepcionServicioModel.objects.filter(encuesta_recepcion_id=value.encuesta_recepcion_id).values_list('pregunta',flat=True)
                cursos = cursoEncuestaRecepcionServicioModel.objects.filter(encuesta_recepcion_id=value.encuesta_recepcion_id,
                                                                            curso__fecha_inicio__range=[fecha_desde,fecha_hasta],
                                                                            curso__fecha_termino__range=[fecha_desde,fecha_hasta])

                list_cursos = []
                list_porcentaje = []
                list_respuestas = []
                for curso in cursos:
                    curso = cursoModel.objects.get(curso_id=curso.curso_id)
                    list_cursos.append(curso)
                    
                    respuestas = respuestaRecepcionServicioModel.objects.filter(encuesta_recepcion_id=value.encuesta_recepcion_id,
                                                                                curso__fecha_inicio__range=[fecha_desde,fecha_hasta],
                                                                                curso__fecha_termino__range=[fecha_desde,fecha_hasta])
                    list_respuestas = []
                    for respuesta in respuestas:
                        list_respuestas.append(respuesta)
                        
                    if not list_respuestas == []:
                        data_porcentaje = {
                            'porc': obtenerResultadoRecepcionServicio(value.encuesta_recepcion_id,curso.curso_id),
                            'curso_id':curso.curso_id
                        }
                        list_porcentaje.append(data_porcentaje)

                data_table = {
                    'encuesta':value,
                    'preguntas':preguntas,
                    'cursos':list_cursos,
                    'respuestas':list_respuestas,
                    'porcentajes':list_porcentaje
                }
                list_encuestas_recepcion.append(data_table)
                
                
            encuestas_alumno = encuestaAlumnoModel.objects.all()
            list_encuestas_alumno = []
            for encuesta in encuestas_alumno:
                preguntas = preguntaAlumnoModel.objects.filter(encuesta_alumno_id=encuesta.encuesta_alumno_id).values_list('pregunta',flat=True)
                cursos = cursoEncuestaAlumnoModel.objects.filter(encuesta_id=encuesta.encuesta_alumno_id,
                                                                 curso__fecha_inicio__range=[fecha_desde,fecha_hasta],
                                                                 curso__fecha_termino__range=[fecha_desde,fecha_hasta])

                list_cursos = []
                list_promedios = []
                list_prom_acumulados = []
                total_promedios = []
                for curso in cursos:
                    curso = cursoModel.objects.get(curso_id=curso.curso_id)
                    list_cursos.append(curso)
                    
                    promedio_acumulado =  round(sum((value['promedio']) 
                                                    for value in obtenerPromedioEncuesta(encuesta.encuesta_alumno_id,curso.curso_id,'alumno'))/preguntas.count(),1)
                    
                    list_prom_acumulados.append({
                        'valor': promedio_acumulado,
                        'curso_id': curso.curso_id
                    })

                    for value in obtenerPromedioEncuesta(encuesta.encuesta_alumno_id,curso.curso_id,'alumno'):
                        list_promedios.append(value)
                        
                    total_promedios = obtenerPromedioTotalEncuesta(encuesta.encuesta_alumno_id,'alumno')
                    
                # promedio_respuestas = respuestaAlumnoModel.objects.values('pregunta').annotate(promedio=Sum('respuesta_valor'))
                # list_respuestas = []
                # for respuesta in promedio_respuestas:
                #     list_respuestas.append(respuesta)

                total_acumulado = sum(prom['valor'] for prom in list_prom_acumulados)

                data_table = {
                    'encuesta': encuesta,
                    'preguntas':preguntas,
                    'cursos':list_cursos,
                    'promedios':list_promedios,
                    'acumulados':list_prom_acumulados,
                    'total_promedios': total_promedios,
                    'total_acumulado': total_acumulado
                }
                list_encuestas_alumno.append(data_table)
                
                
            encuestas_satisfaccion = encuestaSatisfaccionModel.objects.all()
            list_encuestas_satisfaccion = []
            for encuesta in encuestas_satisfaccion:
                preguntas = preguntaSatisfaccionModel.objects.filter(encuesta_id=encuesta.encuesta_id).values_list('pregunta',flat=True)
                cursos = cursoEncuestaSatisfaccionModel.objects.filter(curso_encuesta_id=encuesta.encuesta_id,
                                                                       curso__fecha_inicio__range=[fecha_desde,fecha_hasta],
                                                                       curso__fecha_termino__range=[fecha_desde,fecha_hasta])

                list_cursos = []
                list_promedios = []
                list_prom_acumulados = []
                total_promedios = []
                for curso in cursos:
                    curso = cursoModel.objects.get(curso_id=curso.curso_id)
                    list_cursos.append(curso)

                    respuestas = respuestaSatisfaccionModel.objects.filter(encuesta_id=encuesta.encuesta_id,
                                                                           curso__fecha_inicio__range=[fecha_desde,fecha_hasta],
                                                                           curso__fecha_termino__range=[fecha_desde,fecha_hasta])
                    list_respuestas = []
                    for respuesta in respuestas:
                        list_respuestas.append(respuesta)
                    if not list_respuestas == []:
                        promedio_acumulado =  round(sum((value['promedio']) 
                                                        for value in obtenerPromedioEncuesta(encuesta.encuesta_id,curso.curso_id,'satisfaccion'))/preguntas.count(),1)
                        
                        list_prom_acumulados.append({
                            'valor': promedio_acumulado,
                            'curso_id': curso.curso_id
                        })

                        for value in obtenerPromedioEncuesta(encuesta.encuesta_id,curso.curso_id,'satisfaccion'):
                            list_promedios.append(value)
                            
                        total_promedios = obtenerPromedioTotalEncuesta(encuesta.encuesta_id,'satisfaccion')
                    
                        total_acumulado = sum(prom['valor'] for prom in list_prom_acumulados)
                        
                data_table = {
                    'encuesta': encuesta,
                    'preguntas':preguntas,
                    'cursos':list_cursos,
                    'promedios':list_promedios,
                    'acumulados':list_prom_acumulados,
                    'total_promedios': total_promedios,
                    'total_acumulado': total_acumulado
                }
                list_encuestas_satisfaccion.append(data_table)

            
            data = {
                'encuestas': list_encuestas_recepcion,
                'encuestas_alumnos': list_encuestas_alumno,
                'encuestas_satisfaccion':list_encuestas_satisfaccion
            }
    return render(request, 'resumen/resumen_resultados.html',data)
    
