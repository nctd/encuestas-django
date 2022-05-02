from django.shortcuts import get_object_or_404, render
from django.contrib import messages
from encuestas.models.alumnoModel import alumnoModel
from encuestas.models.encuestaCursoModel import encuestaCursoModel

from encuestas.views.utils.utils import guardarRespuestaEncuestaCurso, validarRespuestaEncuesta, validarCurso

from ..models import cursoModel

from ..forms import EncuestaCursoForm, EncuestaSatisfaccionForm, alumnoCursoForm, alumnoForm


pregunta_1 = 'Se cumplieron los objetivos del curso '
pregunta_2 = 'El contenido del curso fue interesante e importante para su trabajo'
pregunta_3 = 'Intercambio de experiencias entre los participantes '
pregunta_4 = 'Dinámica del curso'
pregunta_5 = 'Ambiente de Trabajo'
pregunta_6 = 'Comunicación y dominio de los contenidos por parte del Relator'
pregunta_7 = 'Puntualidad del Relator'
pregunta_8 = 'Calidad de su manual de trabajo'
pregunta_9 = 'Proyección de la Clase (Contenidos, nitidez, colores)'
pregunta_10 = 'Que le pareció el trato que recibió como cliente'
pregunta_11 = 'Instalaciones (Infraestructura)'
pregunta_12 = 'Servicio de Alimentación.'
pregunta_13 = 'Estimado(a) Participante, si desea agregar algún comentario, que sería de gran utilidad para nosotros, puede escribirlo a continuación:'


def encuesta_curso_view(request):
    cursos = cursoModel.objects.all()

    data = {
        'pregunta_1': pregunta_1,
        'pregunta_2': pregunta_2,
        'pregunta_3': pregunta_3,
        'pregunta_4': pregunta_4,
        'pregunta_5': pregunta_5,
        'pregunta_6': pregunta_6,
        'pregunta_7': pregunta_7,
        'pregunta_8': pregunta_8,
        'pregunta_9': pregunta_9,
        'pregunta_10': pregunta_10,
        'pregunta_11': pregunta_11,
        'pregunta_12': pregunta_12,
        'pregunta_13': pregunta_13,
        'respuestas': ['Deficiente', 'Malo', 'Regular', 'Bueno', 'Excelente'],
        'cursos': cursos
    }
    
    if request.method == 'POST':
        valores_respuestas_m = [request.POST.get('respuesta1', False), request.POST.get('respuesta2', False), 
                                request.POST.get('respuesta3', False), request.POST.get('respuesta4', False),
                                request.POST.get('respuesta5', False), request.POST.get('respuesta6', False),
                                request.POST.get('respuesta7', False), request.POST.get('respuesta8', False),
                                request.POST.get('respuesta9', False), request.POST.get('respuesta10', False),
                                request.POST.get('respuesta11', False), request.POST.get('respuesta12', False)]

        curso = request.POST.get('curso',False)
        nombre_alumno = request.POST.get('nombre_alumno',False)

        data_alumno = {
            'nombre': nombre_alumno.split(' ')[0],
            'a_paterno': nombre_alumno.split(' ')[1],
            'a_materno': nombre_alumno.split(' ')[2],
            'nombre_completo': nombre_alumno,
            'correo': 'correo@correo.com',
        }
        data_encuesta = {
            'curso_id': curso.split('-')[0]
        }


        if(validarRespuestaEncuesta(valores_respuestas_m, 'M') and validarCurso(curso.split('-')[0],curso.split('-')[1])):
            encuesta = EncuestaCursoForm(data=data_encuesta)
            alumno = alumnoForm(data=data_alumno)

            if(encuesta.is_valid() and alumno.is_valid()):
                e_id = encuesta.save()
                a_id = alumno.save()
                data_curso_alumno = {
                    'alumno_id':a_id,
                    'curso_id':curso.split('-')[0]
                }
                alumno_curso = alumnoCursoForm(data=data_curso_alumno)

                if alumno_curso.is_valid():
                    alumno_curso.save()                
                    guardarRespuestaEncuestaCurso(pregunta_1, request.POST['respuesta1'], e_id, a_id)
                    guardarRespuestaEncuestaCurso(pregunta_2, request.POST['respuesta2'], e_id, a_id)
                    guardarRespuestaEncuestaCurso(pregunta_3, request.POST['respuesta3'], e_id, a_id)
                    guardarRespuestaEncuestaCurso(pregunta_4, request.POST['respuesta4'], e_id, a_id)
                    guardarRespuestaEncuestaCurso(pregunta_5, request.POST['respuesta5'], e_id, a_id)
                    guardarRespuestaEncuestaCurso(pregunta_6, request.POST['respuesta6'], e_id, a_id)
                    guardarRespuestaEncuestaCurso(pregunta_7, request.POST['respuesta7'], e_id, a_id)
                    guardarRespuestaEncuestaCurso(pregunta_8, request.POST['respuesta8'], e_id, a_id)
                    guardarRespuestaEncuestaCurso(pregunta_9, request.POST['respuesta9'], e_id, a_id)
                    guardarRespuestaEncuestaCurso(pregunta_10, request.POST['respuesta10'], e_id, a_id)
                    guardarRespuestaEncuestaCurso(pregunta_11, request.POST['respuesta11'], e_id, a_id)
                    guardarRespuestaEncuestaCurso(pregunta_12, request.POST['respuesta12'], e_id, a_id)
                else:
                    get_object_or_404(encuestaCursoModel,e_curso_id=e_id).delete()
                    get_object_or_404(alumnoModel,alumno_id=a_id).delete()
        else:
            print('ERROR AL VALIDAR')
            data['error'] = True
            return render(request,'encuestas/encuesta_curso.html', data)

    else:
        print('nopost')
    return render(request, 'encuestas/encuesta_curso.html', data)

