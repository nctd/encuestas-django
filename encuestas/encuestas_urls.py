from encuestas.views.error import error400Handler
from .views.encuesta_satisfaccion_view import encuesta_satisfaccion_view
from .views.encuesta_curso_view import encuesta_curso_view
from .views.home import home

from django.urls import path

from django.conf.urls import handler400

urlpatterns = [
    path('',home,name='home'),
    path('encuesta_satisfaccion/<encuesta_id>/<curso_id>/', encuesta_satisfaccion_view, name='encuesta_satisfaccion'),
    # path('encuesta_curso/<encuesta_id>/', encuesta_curso_view, name='encuesta_curso'),
    path('encuesta_curso/<encuesta_id>/<curso_id>/', encuesta_curso_view, name='encuesta_curso'),
]

handler400 = error400Handler.as_view()