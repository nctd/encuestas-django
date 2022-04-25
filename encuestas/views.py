from django.shortcuts import render

from .forms import EncuestaSatisfaccionForm
# Create your views here.


def home(request):

    if request.method == 'POST':
        form = EncuestaSatisfaccionForm(data=request.POST)
        if form.is_valid():
            form.save()
        # data['form'] = form
    else:
        form = EncuestaSatisfaccionForm()
    return render(request, 'index.html',{'form':form})
