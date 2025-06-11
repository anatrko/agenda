from django.shortcuts import render, redirect, get_object_or_404
from .models import Evento
from .forms import EventoForm
from django.utils import timezone

def lista_eventos(request):
    eventos = Evento.objects.all().order_by('data')
    return render(request, 'eventos/lista_eventos.html', {'eventos': eventos})

def criar_evento(request):
    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_eventos')
    else:
        form = EventoForm()
    return render(request, 'eventos/criar_evento.html', {'form': form})

def editar_evento(request, id):
    evento = get_object_or_404(Evento, id=id)
    if request.method == 'POST':
        form = EventoForm(request.POST, instance=evento)
        if form.is_valid():
            form.save()
            return redirect('lista_eventos')
    else:
        form = EventoForm(instance=evento)
    return render(request, 'eventos/editar_evento.html', {'form': form, 'evento': evento})

def excluir_evento(request, id):
    evento = get_object_or_404(Evento, id=id)
    if request.method == 'POST':
        evento.delete()
        return redirect('lista_eventos')
    return render(request, 'eventos/excluir_evento.html', {'evento': evento})
