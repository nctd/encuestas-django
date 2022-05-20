from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from encuestas.models.cursoEncuestaRecepcionServicioModel import cursoEncuestaRecepcionServicioModel
from encuestas.models.cursoModel import cursoModel
from encuestas.models.encuestaRecepcionServicio import encuestaRecepcionServicioModel
from encuestas.models.preguntaRecepcionServicio import preguntaRecepcionServicioModel

from encuestas.models.respuestaRecepcionServicioModel import respuestaRecepcionServicioModel
from encuestas.views.utils.utils import obtenerResultadoRecepcionServicio

def resumen_resultados_view(request):
    current_user = request.user
    if not current_user.is_superuser:
        return redirect('home')
    
    encuestas = encuestaRecepcionServicioModel.objects.all()

    list_encuestas = []
    for value in encuestas:
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
            'preguntas':preguntas,
            'cursos':list_cursos,
            'respuestas':list_respuestas,
            'porcentajes':list_porcentaje
        }
        list_encuestas.append(data_table)

        # print(list_encuestas)
    # print(list_encuestas)
    # encuestas_recepcion_servicio = cursoEncuestaRecepcionServicioModel.objects.all()
    # list_recepcion_servicio = []
    # for value in encuestas_recepcion_servicio:
    #     curso = cursoModel.objects.get(curso_id=value.curso_id)
    #     data_curso = {
    #         'curso': curso,
    #     }
    #     list_recepcion_servicio.append(data_curso)

    #     for item in respuestaRecepcionServicioModel.objects.filter(curso_id=value):
    #         resp_recep_serv = {
    #             'curso':curso,
    #             'pregunta': item.pregunta,
    #             'respuesta': item.respuesta_valor
    #         }
    # print(list_recepcion_servicio)
    data = {
        # 'recepcion_servicio':list_recepcion_servicio,
        'encuestas': list_encuestas
    }
    return render(request, 'resumen/resumen_resultados.html',data)