from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Sum,Count,Avg
from encuestas.models.alumnoCursoModel import alumnoCursoModel

from encuestas.models.cursoEncuestaAlumnoModel import cursoEncuestaAlumnoModel
from encuestas.models.cursoEncuestaRecepcionServicioModel import cursoEncuestaRecepcionServicioModel
from encuestas.models.cursoModel import cursoModel
from encuestas.models.encuestaAlumnoModel import encuestaAlumnoModel
from encuestas.models.encuestaRecepcionServicio import encuestaRecepcionServicioModel
from encuestas.models.preguntaAlumnoModel import preguntaAlumnoModel
from encuestas.models.preguntaRecepcionServicio import preguntaRecepcionServicioModel
from encuestas.models.respuestaAlumnoModel import respuestaAlumnoModel

from encuestas.models.respuestaRecepcionServicioModel import respuestaRecepcionServicioModel
from encuestas.views.utils.utils import obtenerPromedioEncuestaAlumno, obtenerResultadoRecepcionServicio

def resumen_resultados_view(request):
    current_user = request.user
    if not current_user.is_superuser:
        return redirect('home')
    
    encuestas_recepcion = encuestaRecepcionServicioModel.objects.all()

    list_encuestas_recepcion = []
    for value in encuestas_recepcion:
        preguntas = preguntaRecepcionServicioModel.objects.filter(encuesta_recepcion_id=value.encuesta_recepcion_id).values_list('pregunta',flat=True)
        cursos = cursoEncuestaRecepcionServicioModel.objects.filter(encuesta_recepcion_id=value.encuesta_recepcion_id)
        list_cursos = []
        list_porcentaje = []
        for curso in cursos:
            curso = cursoModel.objects.get(curso_id=curso.curso_id)
            list_cursos.append(curso)
            data_porcentaje = {
                'porc': obtenerResultadoRecepcionServicio(value.encuesta_recepcion_id,curso.curso_id),
                'curso_id':curso.curso_id
            }
            list_porcentaje.append(data_porcentaje)
        respuestas = respuestaRecepcionServicioModel.objects.filter(encuesta_recepcion_id=value.encuesta_recepcion_id)
        list_respuestas = []
        for respuesta in respuestas:
            list_respuestas.append(respuesta)
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
        cursos = cursoEncuestaAlumnoModel.objects.filter(encuesta_id=encuesta.encuesta_alumno_id)
        list_cursos = []
        list_promedios = []
        list_prom_acumulados = []
        for curso in cursos:
            curso = cursoModel.objects.get(curso_id=curso.curso_id)
            list_cursos.append(curso)
            
            promedio_acumulado =  round(sum((value['promedio']) 
                                            for value in obtenerPromedioEncuestaAlumno(encuesta.encuesta_alumno_id,curso.curso_id))/preguntas.count(),2)
            list_prom_acumulados.append({
                'valor': promedio_acumulado,
                'curso_id': curso.curso_id
            })

            
            for value in obtenerPromedioEncuestaAlumno(encuesta.encuesta_alumno_id,curso.curso_id):
                list_promedios.append(value)
                
        promedio_respuestas = respuestaAlumnoModel.objects.values('pregunta').annotate(promedio=Sum('respuesta_valor'))
        for respuesta in promedio_respuestas:
            list_respuestas.append(respuesta)
            
        data_table = {
            'encuesta': encuesta,
            'preguntas':preguntas,
            'cursos':list_cursos,
            'promedios':list_promedios,
            'acumulados':list_prom_acumulados
        }
        list_encuestas_alumno.append(data_table)

    data = {
        'encuestas': list_encuestas_recepcion,
        'encuestas_alumnos': list_encuestas_alumno
    }
    return render(request, 'resumen/resumen_resultados.html',data)