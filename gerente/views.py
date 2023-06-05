from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages

from .models import (UserProfile)
from .forms import (Login, Registro)

#Controladores
def loginView(request):

    if request.user.is_superuser:
        return redirect('/admin')
    elif not request.user.is_anonymous: 
        return redirect('root:inicio')
    
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        try:
            usuario = UserProfile.objects.get(email=email)
            if usuario is not None and usuario.check_password(password):
                login(request, usuario)
                return redirect('/admin') if usuario.is_superuser else redirect('root:inicio')
            else:
                print(usuario.is_superuser)
                messages.error(request, "Contraseña incorrecta")
        except Exception as e:
            messages.error( request, "Lo sentimos, no pudimos encontrar tu cuenta")
            usuario = None
            print(e)
    form = Login()
    return render(request, 'login.html', {'form': form})

def registro(request):
    if request.method == 'POST':
        email = request.POST['email']
        form = Registro(request.POST)
        if form.is_valid():
            form.save()
            user = UserProfile.objects.get(email=email)
            login(request, user)
            return redirect('root:login')
    else:
        form = Registro()
    context = {'form': form}
    return render(request, 'registro.html', context)

def index(request):
    return render(request, 'index.html')

def inicio(request):
    return render(request, 'inicio.html')
