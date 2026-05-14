from django.shortcuts import render, redirect
from .forms import AutoForm
from .models import Auto
from django.shortcuts import get_object_or_404

from django.contrib.auth.decorators import login_required

def inicio(request):
    return render(request, "autos/inicio.html")

def crear_auto(request):
    if request.method == 'POST':
        form = AutoForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('lista_autos')

    else:
        form = AutoForm()

    return render(request, 'autos/crear.html', {'form': form})

def lista_autos(request):
    autos = Auto.objects.all()
    return render(request, "autos/lista.html", {"autos": autos})

def buscar(request):
    query = request.GET.get("q")
    autos = Auto.objects.filter(marca__icontains=query)
    return render(request, "autos/lista.html", {"autos": autos})

def detalle_auto(request, id):
    auto = get_object_or_404(Auto, id=id)

    return render(request, 'autos/detalle.html', {
        'auto': auto
    })

@login_required

def editar_auto(request, id):
    auto = get_object_or_404(Auto, id=id)

    if request.method == 'POST':
        form = AutoForm(request.POST, request.FILES, instance=auto)

        if form.is_valid():
            form.save()
            return redirect('lista_autos')

    else:
        form = AutoForm(instance=auto)

    return render(request, 'autos/editar.html', {
        'form': form
    })

@login_required

def borrar_auto(request, id):
    auto = get_object_or_404(Auto, id=id)

    if request.method == 'POST':
        auto.delete()
        return redirect('lista_autos')

    return render(request, 'autos/borrar.html', {
        'auto': auto
    })

def about(request):
    return render(request, 'autos/about.html')