from django import forms
from .models import Evento

class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ['titulo', 'descricao', 'data']
        widgets = {
            'data': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }