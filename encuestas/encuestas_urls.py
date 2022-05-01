from .views.encuesta_satisfaccion_view import encuesta_satisfaccion_view
from .views.encuesta_curso_view import encuesta_curso_view
from .views.home import home

from django.urls import path

urlpatterns = [
    path('',home,name='home'),
    path('encuesta_satisfaccion', encuesta_satisfaccion_view, name='encuesta_satisfaccion'),
    path('encuesta_curso', encuesta_curso_view, name='encuesta_curso'),
]
