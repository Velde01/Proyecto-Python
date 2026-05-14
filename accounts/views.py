from django.shortcuts import render, redirect
from .forms import RegistroForm
from .models import Perfil
from django.contrib.auth.decorators import login_required
from .forms import PerfilForm

def registro(request):

    if request.method == 'POST':
        form = RegistroForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')

    else:
        form = RegistroForm()

    return render(request, 'accounts/registro.html', {
        'form': form
    })

@login_required
def perfil(request):

    perfil, created = Perfil.objects.get_or_create(
        user=request.user
    )

    return render(request, 'accounts/perfil.html', {
        'perfil': perfil
    })

@login_required
def editar_perfil(request):

    perfil, created = Perfil.objects.get_or_create(
        user=request.user
    )

    if request.method == 'POST':

        form = PerfilForm(
            request.POST,
            request.FILES,
            instance=perfil
        )

        if form.is_valid():
            form.save()
            return redirect('perfil')

    else:
        form = PerfilForm(instance=perfil)

    return render(request, 'accounts/editar_perfil.html', {
        'form': form
    })