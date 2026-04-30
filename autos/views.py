from django.shortcuts import render
from .models import Auto
from .forms import AutoForm

def inicio(request):
    return render(request, "autos/inicio.html")

def crear_auto(request):
    form = AutoForm(request.POST or None)
    if form.is_valid():
        form.save()

    return render(request, "autos/crear.html", {"form": form})

def lista_autos(request):
    autos = Auto.objects.all()
    return render(request, "autos/lista.html", {"autos": autos})

def buscar(request):
    query = request.GET.get("q")
    autos = Auto.objects.filter(marca__icontains=query)
    return render(request, "autos/lista.html", {"autos": autos})