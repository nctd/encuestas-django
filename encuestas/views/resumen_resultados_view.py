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
from encuestas.views.utils.resumen_encuestas.resumen_encuesta_alumnos import obtenerResumenAlumnos
from encuestas.views.utils.resumen_encuestas.resumen_encuesta_recepcion import obtenerResumenRecepcionServicio
from encuestas.views.utils.resumen_encuestas.resumen_encuesta_satisfaccion import obtenerResumenSatisfaccion
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

            data = {
                'encuestas': obtenerResumenRecepcionServicio(fecha_desde,fecha_hasta),
                'encuestas_alumnos': obtenerResumenAlumnos(fecha_desde,fecha_hasta),
                'encuestas_satisfaccion':obtenerResumenSatisfaccion(fecha_desde,fecha_hasta)
            }
    return render(request, 'resumen/resumen_resultados.html',data)
    
