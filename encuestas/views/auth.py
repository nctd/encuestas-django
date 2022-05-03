from django.shortcuts import redirect, render
from django.contrib import messages,auth

from ..forms import CustomUserCreationForm

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None and user.is_active:
            auth.login(request, user)
            return redirect('')
        else:
            messages.error(request,'Nombre de usuario y/o contraseña incorrectos')
            return redirect('login')
            # return HttpResponse("Invalid login. Please try again.")
    return render(request, 'auth/login_user.html')

def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)

        if formulario.is_valid():
            formulario.save()

            return redirect(to='/auth/login_user?register=true')
        data['form'] = formulario
    return render(request,'auth/registro.html',data) 