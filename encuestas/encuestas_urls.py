from os import name
from encuestas.views import encuesta_satisfaccion_view
from django.urls import path

urlpatterns = [
    path('', encuesta_satisfaccion_view, name='encuesta_satisfaccion_view'),
]
