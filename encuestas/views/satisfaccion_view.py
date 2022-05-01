from django.shortcuts import render
from ..models.catalogoModel import catalogoModel

# def encuesta_view(request):
#     preguntas = catalogoModel.objects.filter(nombre='encuesta_satisfaccion').order_by('orden').values_list('pregunta',flat=True)
#     opciones = catalogoModel.objects.filter(nombre='encuesta_satisfaccion',tipo='satisfaccion').first()
#     print(preguntas)
#     print(opciones)
#     data = {
#         'preguntas':preguntas,
#         'opciones': opciones
#     }
#     return render(request, 'encuesta_satisfaccion.html',data)