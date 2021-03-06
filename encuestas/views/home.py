from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from encuestas.models.alumnoCursoModel import alumnoCursoModel
from encuestas.models.alumnoModel import alumnoModel
from encuestas.models.cursoEncuestaAlumnoModel import cursoEncuestaAlumnoModel
from encuestas.models.cursoEncuestaRecepcionServicioModel import cursoEncuestaRecepcionServicioModel
from encuestas.models.cursoEncuestaSatisfaccionModel import cursoEncuestaSatisfaccionModel


from encuestas.models.cursoModel import cursoModel
from encuestas.models.empresaModel import empresaModel
from encuestas.models.encuestaAlumnoModel import encuestaAlumnoModel
from encuestas.models.encuestaRecepcionServicio import encuestaRecepcionServicioModel
from encuestas.models.encuestaSatisfaccionModel import encuestaSatisfaccionModel
from encuestas.models.respuestaAlumnoModel import respuestaAlumnoModel
from encuestas.models.respuestaRecepcionServicioModel import respuestaRecepcionServicioModel
from encuestas.models.respuestaSatisfaccionModel import respuestaSatisfaccionModel


@login_required(login_url='/auth/login_user')
def home(request):
    current_user = request.user
    print()
    if current_user.is_superuser:
        return redirect('resumen_resultados')
    
    if not current_user.es_empresa and not current_user.es_alumno:
        return redirect('login')
    
    if current_user.es_empresa:
        try:
            empresa = empresaModel.objects.get(user=current_user.id)
            curso = cursoModel.objects.filter(empresa_id=empresa.empresa_id)
            
            lista_encuestas = []
            for item in curso:
                curso_encuesta = cursoEncuestaSatisfaccionModel.objects.filter(curso_id=item.curso_id)
                for value in curso_encuesta:
                    encuesta = encuestaSatisfaccionModel.objects.get(encuesta_id=value.encuesta_id)
                    estado = respuestaSatisfaccionModel.objects.filter(encuesta=encuesta.encuesta_id,curso=item.curso_id).exists()

                    data_encuesta = {
                        'estado': estado,
                        'nombre_curso': item.nombre_curso,
                        'nombre_encuesta': encuesta.nombre,
                        'curso_id': value.curso_id,
                        'encuesta_id': value.encuesta_id
                    }
                    lista_encuestas.append(data_encuesta)
            
            lista_recepcion = []
            for item in curso:
                curso_recepcion = cursoEncuestaRecepcionServicioModel.objects.filter(curso_id=item.curso_id)
                for value in curso_recepcion:
                    encuesta = encuestaRecepcionServicioModel.objects.get(encuesta_recepcion_id=value.encuesta_recepcion_id)
                    estado = respuestaRecepcionServicioModel.objects.filter(encuesta_recepcion_id=encuesta.encuesta_recepcion_id,
                                                                            curso=item.curso_id).exists()
                    data_recepcion = {
                        'estado': estado,
                        'nombre_curso': item.nombre_curso,
                        'nombre_encuesta': encuesta.nombre,
                        'curso_id': value.curso_id,
                        'encuesta_id': value.encuesta_recepcion_id                        
                    }
                    lista_recepcion.append(data_recepcion)
            data = {
                'lista_encuestas': lista_encuestas,
                'lista_recepcion':lista_recepcion,
                'empresa': True
            }

            return render(request,'index.html',data)
        except empresaModel.DoesNotExist:
            data = {
                'error': True,
                'mensaje': 'El usuario no esta asociado a una empresa, por favor contacte al administrador',
                'status': 404,
                'error_empresa': True
            }
            return render(request, 'error/error.html',data, status=404)
        
    if current_user.es_alumno:
        try:
            alumno = alumnoModel.objects.get(user=current_user.id)
            alumno_cursos = alumnoCursoModel.objects.filter(alumno_id=alumno.alumno_id)
            lista_encuestas = []

            for item in alumno_cursos:
                encuestas_curso = cursoEncuestaAlumnoModel.objects.filter(curso_id=item.curso_id)
                curso = cursoModel.objects.get(curso_id=item.curso_id)
                for value in encuestas_curso:
                    encuesta = encuestaAlumnoModel.objects.get(encuesta_alumno_id=value.encuesta_id)
                    
                    estado = respuestaAlumnoModel.objects.filter(encuesta_alumno=encuesta.encuesta_alumno_id,alumno_curso=item.alumno_curso_id).exists()
                
                    data_encuesta = {
                        'estado': estado,
                        'nombre_curso': curso.nombre_curso,
                        'nombre_encuesta': encuesta.nombre,
                        'curso_id': curso.curso_id,
                        'encuesta_id': encuesta.encuesta_alumno_id
                    }
                    lista_encuestas.append(data_encuesta)
                
            data = {
                'lista_encuestas': lista_encuestas,
                'alumno': True
            }

            return render(request,'index.html',data)
        except alumnoModel.DoesNotExist:
            # return HttpResponse(request,'EL ALUMNO NO EXISTE')
            data = {
                'error': True,
                'mensaje': 'El usuario no es un alumno, por favor contacte al administrador',
                'status': 404,
                'error_alumno': True
            }
            return render(request, 'error/error.html',data, status=404)
