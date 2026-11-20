from django import forms
from .models import Servicio

class ServicioForm(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = ['titulo', 'descripcion', 'activo']
        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'input-pro',
                'placeholder': 'Ej. Citas de Salud, Seguridad Ciudadana...'
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'input-pro',
                'rows': 3,
                'placeholder': 'Describe brevemente el servicio comunitario...'
            }),
            'activo': forms.CheckboxInput(attrs={'class': 'check-pro'}),
        }