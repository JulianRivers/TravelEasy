from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from gerente.models import (Evento)
# Controladores del empleado

@login_required
def inicio(request):
    """
    root:inicio
    """
    user = request.user
    eventos = Evento.objects.filter(asistenciaevento__usuario=user)
    context = {
        'eventos': eventos
    }
    return render(request, 'inicio.html', context)
