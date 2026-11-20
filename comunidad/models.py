from django.db import models

class Servicio(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(default="Servicio disponible para la comunidad.")
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo