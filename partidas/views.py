from django.shortcuts import render, redirect
from partidas.models import Capitulo, Partida
from partidas.forms import CapituloForm, PartidaForm
from django.contrib.auth.decorators import permission_required, login_required
from django.shortcuts import get_object_or_404, redirect
from presupuestos.models import Presupuesto
from datetime import datetime, timedelta
import django.utils.timezone as timezone

# vistas de capitulos


@login_required
def lista_capitulos(request):
    capitulos = Capitulo.objects.all()
    return render(request, 'lista_capitulos.html', {'capitulos': capitulos})


@login_required
@permission_required('capitulos.add_capitulo', raise_exception=True)
def nuevo_capitulo(request):
    form = CapituloForm
    if request.method == 'POST':
        form = CapituloForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('capitulos:lista')
    else:
        form = CapituloForm()

    return render(request, 'nuevo_capitulo.html', {'form': form})


@login_required
@permission_required('capitulos.delete_capitulo', raise_exception=True)
def eliminar_capitulo(request, clave):
    partida = Capitulo.objects.get(clave=clave)
    partida.delete()
    return redirect('capitulos:lista')


@login_required
@permission_required('capitulos.change_capitulo', raise_exception=True)
def editar_capitulo(request, clave):
    capitulo = Capitulo.objects.get(clave=clave)
    if request.method == 'POST':
        form = CapituloForm(request.POST, instance=capitulo)
        if form.is_valid():
            form.save()
            return redirect('capitulos:lista')
    else:
        form = CapituloForm(instance=capitulo)
    return render(request, 'editar_capitulo.html', {'form': form})


# vistas de partidas
@login_required
def lista_partidas(request):
    partidas = Partida.objects.all()
    return render(request, 'lista_partidas.html', {'partidas': partidas})


@login_required
@permission_required('partidas.add_partida', raise_exception=True)
def nueva_partida(request):
    form = PartidaForm
    if request.method == 'POST':
        form = PartidaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('partidas:lista')
    else:
        form = PartidaForm()
    return render(request, 'nueva_partida.html', {'form': form})

@login_required
@permission_required('partidas.add_partida', raise_exception=True)
def nueva_partida_especifica(request, id):
    capitulo = Capitulo.objects.get(clave=id)
    context = {}
    initial_dict = {
        "capitulo" : capitulo.clave,
    }

    form = PartidaForm(initial = initial_dict)
    context['form']= form

    if request.method == 'POST':
        form = PartidaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('principal:principal')
    else:
        form = PartidaForm()
    return render(request, 'nueva_partida.html', context)

@login_required
@permission_required('partidas.change_partida', raise_exception=True)
def editar_partida(request, clave):
    partida = Partida.objects.get(clave=clave)
    if request.method == 'POST':
        form = PartidaForm(request.POST, instance=partida)
        if form.is_valid():
            form.save()
            return redirect('partidas:lista')
    else:
        form = PartidaForm(instance=partida)
    return render(request, 'editar_partida.html', {'form': form})


@login_required
@permission_required('partidas.delete_partida', raise_exception=True)
def eliminar_partida(request, clave):
    partida = Partida.objects.get(clave=clave)
    partida.delete()
    return redirect('partidas:lista')

def aniosesion(request):
    presupuesto = get_object_or_404(Presupuesto)
    anio = timezone.now().year
    anio
    request.session['anio'] = presupuesto.anio
    print(request.session['anio'])
    print("hola")
    print(anio)
    
    context = {'anio': anio}
    return redirect(request, 'partidas:sesion', context)