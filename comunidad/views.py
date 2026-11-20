from django.shortcuts import render
from django.http import HttpResponse
from .models import Servicio

def hola_mundo(request):
    return HttpResponse("<h1>¡Hola Mundo desde Django!</h1><p>Aplicación ComunidadConectada funcionando.</p>")

def listar_servicios(request):
    items = Servicio.objects.all()
    return render(request, 'comunidad/lista.html', {'servicios': items})