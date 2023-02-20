from django.shortcuts import render, redirect
from .forms import Login
from django.contrib.auth import login
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            usuario = User.objects.get(username=username)
            if usuario is not None and usuario.check_password(password):
                login(request, usuario)
                return redirect('asesor:inicio')
            else:
                print('hola')
                #messages.error(request, "Contraseña incorrecta")
        except Exception as e:
            #messages.error( request, "Lo sentimos, no pudimos encontrar tu cuenta")
            usuario = None
            print(e)
    form = Login()
    return render(request, 'index.html', {'form': form})

def inicio(request):
    return render(request, 'inicio.html')