from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_servicios, name='listar_servicios'),
    path('hola/', views.hola_mundo, name='hola_mundo'),
]