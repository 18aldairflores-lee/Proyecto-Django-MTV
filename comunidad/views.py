from django.shortcuts import render, redirect, get_object_or_404
from .models import Servicio
from .forms import ServicioForm

def hola_mundo(request):
    return render(request, 'comunidad/hola.html')

def listar_servicios(request):
    items = Servicio.objects.all().order_by('-id')
    total = items.count()
    activos = items.filter(activo=True).count()
    return render(request, 'comunidad/lista.html', {
        'servicios': items,
        'total': total,
        'activos': activos,
    })

def crear_servicio(request):
    if request.method == 'POST':
        form = ServicioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_servicios')
    else:
        form = ServicioForm()
    return render(request, 'comunidad/crear.html', {'form': form})

def cambiar_estado(request, pk):
    servicio = get_object_or_404(Servicio, pk=pk)
    servicio.activo = not servicio.activo
    servicio.save()
    return redirect('listar_servicios')