from django.shortcuts import render
from django.views.generic import TemplateView

# def errorHandler(request):
#     return render(request,'error/error.html',status=400)

class error400Handler(TemplateView):
    template_name = 'error/error.html'