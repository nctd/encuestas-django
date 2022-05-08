from django.http import HttpResponse
from django.shortcuts import render
from encuestas.models.alumnoCursoModel import alumnoCursoModel
from encuestas.models.alumnoModel import alumnoModel


from encuestas.models.cursoModel import cursoModel
from encuestas.models.empresaModel import empresaModel
from encuestas.models.encuestaCursoModel import encuestaCursoModel
from encuestas.models.encuestaSatisfaccionModel import encuestaSatisfaccionModel
from encuestas.models.respuestaCursoModel import respuestaCursoModel
from encuestas.models.respuestaSatisfaccionModel import respuestaSatisfaccionModel



def home(request):
    current_user = request.user
    if current_user.es_empresa:
        try:
            empresa = empresaModel.objects.get(user=current_user.id)
            curso = cursoModel.objects.filter(resp_cliente=empresa.empresa_id)
            
            lista_encuestas = []
            for item in curso:
                encuesta = encuestaSatisfaccionModel.objects.get(curso=item.curso_id)
                estado = respuestaSatisfaccionModel.objects.filter(encuesta=encuesta.encuesta_id).exists()

                data_encuesta = {
                    'estado': estado,
                    'nombre_curso': item.nombre_curso,
                    'curso_id': item.curso_id
                }
                lista_encuestas.append(data_encuesta)
                
            data = {
                'lista_encuestas': lista_encuestas
            }

            return render(request,'index.html',data)
        except:
            return render(request,'index.html')
        
    if current_user.es_alumno:
        try:
            alumno = alumnoModel.objects.get(user=current_user.id)
            alm_cursos = alumnoCursoModel.objects.filter(alumno_id=alumno.alumno_id)
            
            lista_encuestas = []

            for item in alm_cursos:
                print(item.curso_id)
                curso = cursoModel.objects.filter(curso_id=item.curso_id)
                print('*****************')
                print(curso)
                encuesta = encuestaCursoModel.objects.get(curso=item.curso_id)
                estado = respuestaCursoModel.objects.filter(encuesta=encuesta.encuesta_id).exists()
                data_encuesta = {
                    'estado': estado,
                    'nombre_curso': item.nombre_curso,
                    'curso_id': item.curso_id
                }
                lista_encuestas.append(data_encuesta)
                
            data = {
                'lista_encuestas': lista_encuestas
            }

            return render(request,'index.html',data)
        except alumnoModel.DoesNotExist:
            return HttpResponse(request,'EL ALUMNO NO EXISTE')
            # return render(request,'index.html')