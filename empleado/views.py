from django.shortcuts import (render, redirect, get_object_or_404)
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from gerente.models import (Evento, Viatico)
from django.http import JsonResponse
from .forms import (AgregarViatico)
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
def agregarViatico(request, idEvento:int):
    """
    Pagina donde se agrega la información de los viaticos
    name= "empleado:inicio"
    """
    evento = get_object_or_404(Evento, id=idEvento)
    if request.method == 'POST':
        form = AgregarViatico(request.POST, request.FILES)
        if form.is_valid():
            viatico = form.save(commit=False)
            viatico.evento = evento
            viatico.verificado=False
            viatico.save()
            return redirect('empleado:evento', idEvento=evento.id)        
    else:
        form = AgregarViatico()
    context = {
        'form': form,
        'evento': evento,
    }
    return render(request, 'agregar-viatico.html', context)


@csrf_exempt
def mi_vista_ajax(request):
    if request.method == 'POST':
        # Procesa la solicitud AJAX
        # Realiza cualquier operación necesaria en el servidor
        data = {'message': 'Solicitud AJAX recibida correctamente'}
        return JsonResponse(data)

