from django.shortcuts import render

from .forms import EncuestaSatisfaccionForm
# Create your views here.


def encuesta_satisfaccion_view(request):
    if request.method == 'POST':
        print('TEST')
        for value in request.POST:
            # print(value)
            print(request.POST['respuesta1'])
        # form = EncuestaSatisfaccionForm(data=request.POST)
        # if form.is_valid():
            # form.save()
        # data['form'] = form
    else:
        print('nopost')
        # form = EncuestaSatisfaccionForm()
    # return render(request, 'index.html',{'form':form})
    return render(request, 'index.html')
