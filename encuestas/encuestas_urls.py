from os import name
from .views.encuesta_satisfaccion_view import encuesta_satisfaccion_view
# from .views.satisfaccion_view import encuesta_view
from django.urls import path

urlpatterns = [
    path('', encuesta_satisfaccion_view, name='encuesta_satisfaccion_view'),
]
