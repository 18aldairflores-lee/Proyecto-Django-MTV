from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_servicios, name='listar_servicios'),
    path('crear/', views.crear_servicio, name='crear_servicio'),
    path('estado/<int:pk>/', views.cambiar_estado, name='cambiar_estado'),
    path('hola/', views.hola_mundo, name='hola_mundo'),
]