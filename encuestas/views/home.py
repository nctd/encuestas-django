from django.http import HttpResponse
from django.shortcuts import redirect, render


from encuestas.models.alumnoCursoModel import alumnoCursoModel
from encuestas.models.alumnoModel import alumnoModel
from encuestas.models.cursoEncuestaModel import cursoEncuestaModel


from encuestas.models.cursoModel import cursoModel
from encuestas.models.empresaModel import empresaModel
from encuestas.models.encuestaAlumnoModel import encuestaAlumnoModel
from encuestas.models.encuestaSatisfaccionModel import encuestaSatisfaccionModel
from encuestas.models.respuestaAlumnoModel import respuestaAlumnoModel
from encuestas.models.respuestaSatisfaccionModel import respuestaSatisfaccionModel



def home(request):
    current_user = request.user
    if current_user.es_empresa:
        try:
            empresa = empresaModel.objects.get(user=current_user.id)
            curso = cursoModel.objects.filter(empresa_id=empresa.empresa_id)
            
            lista_encuestas = []
            for item in curso:
                print(item)
                curso_encuesta = cursoEncuestaModel.objects.get(curso_id=item.curso_id)
                encuesta = encuestaSatisfaccionModel.objects.get(encuesta_id=curso_encuesta.encuesta_id)
                estado = respuestaSatisfaccionModel.objects.filter(encuesta=encuesta.encuesta_id).exists()

                data_encuesta = {
                    'estado': estado,
                    'nombre_curso': item.nombre_curso,
                    'encuesta_id': curso_encuesta.encuesta_id
                }
                lista_encuestas.append(data_encuesta)
                
            data = {
                'lista_encuestas': lista_encuestas,
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
            alm_cursos = alumnoCursoModel.objects.filter(alumno_id=alumno.alumno_id)
            
            lista_encuestas = []

            for item in alm_cursos:
                curso = cursoModel.objects.get(curso_id=item.curso_id)
                encuesta = encuestaAlumnoModel.objects.get(alumno_curso=item.al_cu_id)
                estado = respuestaAlumnoModel.objects.filter(encuesta_curso=encuesta.enc_curso_id).exists()
                
                data_encuesta = {
                    'estado': estado,
                    'nombre_curso': curso.nombre_curso,
                    'encuesta_id': encuesta.enc_curso_id
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
        
    if not current_user.es_empresa and not current_user.es_alumno:
        return render(request,'index.html')
