from django.shortcuts import render


from encuestas.models.cursoModel import cursoModel
from encuestas.models.empresaModel import empresaModel
from encuestas.models.encuestaSatisfaccionModel import encuestaSatisfaccionModel
from encuestas.models.respuestaSatisfaccionModel import respuestaSatisfaccionModel



def home(request):
    current_user = request.user
    try:
        empresa = empresaModel.objects.get(user=current_user.id)
        curso = cursoModel.objects.get(resp_cliente=empresa.empresa_id)
        encuesta = encuestaSatisfaccionModel.objects.get(curso=curso.curso_id)
        estado_encuesta = respuestaSatisfaccionModel.objects.filter(encuesta=encuesta.encuesta_id).exists()
        print(estado_encuesta)
        data = {
            'estado_encuesta':estado_encuesta,
            'curso': curso,
            'encuesta': encuesta
        }
        return render(request,'index.html',data)
    except:
        return render(request,'index.html')