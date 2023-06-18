from django.shortcuts import (render, get_object_or_404)
from django.contrib.auth.decorators import login_required
from gerente.models import (Evento, Viatico)
from django.http import JsonResponse
# Controladores del empleado

@login_required
def inicio(request):
    """
    Página de inicio donde el empleado ve todos los eventos a los que está asociado
    name: "empleado:inicio"
    """
    user = request.user
    eventos = Evento.objects.filter(asistenciaevento__usuario=user)
    context = {
        'eventos': eventos
    }
    return render(request, 'eventos.html', context)

@login_required
def evento(request, idEvento:int):
    """
    Página donde se ven los viaticos en detalle del evento
    name = "empleado:evento"
    """
    evento = get_object_or_404(Evento, id=idEvento)
    viaticos = Viatico.objects.filter(evento=evento)

    context = {
        'evento': evento,
        'viaticos': viaticos
    }
    return render(request, 'eventos-detalle.html', context)

@login_required
def evento(request, idEvento:int):
    """
    Página donde se ven los viaticos en detalle del evento
    name = "empleado:evento"
    """
    evento = get_object_or_404(Evento, id=idEvento)
    viaticos = Viatico.objects.filter(evento=evento)

    context = {
        'evento': evento,
        'viaticos': viaticos
    }
    return render(request, 'eventos-detalle.html', context)

@login_required
def agregarViatico(request, idEvento:int):
    """
    Pagina donde se agrega la información de los viaticos
    name= "empleado:inicio"
    """
    if request.method == 'GET':
        return render(request, 'agregar-viatico.html')
    
    user = request.user
    eventos = Evento.objects.filter(asistenciaevento__usuario=user)
    context = {
        'eventos': eventos
    }
    return JsonResponse({'status': 'success'})

