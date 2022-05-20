from encuestas.views.encuesta_recepcion_servicio_view import encuesta_recepcion_servicio_view
from encuestas.views.error import error400Handler
from encuestas.views.resumen_resultados_view import resumen_resultados_view
from .views.encuesta_satisfaccion_view import encuesta_satisfaccion_view
from .views.encuesta_curso_view import encuesta_curso_view
from .views.home import home

from django.urls import path

from django.conf.urls import handler400

urlpatterns = [
    path('',home,name='home'),
    path('encuesta_satisfaccion/<encuesta_id>/<curso_id>/', encuesta_satisfaccion_view, name='encuesta_satisfaccion'),
    path('encuesta_curso/<encuesta_id>/<curso_id>/', encuesta_curso_view, name='encuesta_curso'),
    path('encuesta_recepcion_servicio/<encuesta_id>/<curso_id>/', encuesta_recepcion_servicio_view, name='encuesta_recepcion_servicio'),
    path('resultados',resumen_resultados_view,name='resumen_resultados')
]

handler400 = error400Handler.as_view()