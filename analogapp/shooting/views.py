from django.shortcuts import render, redirect
from .models import Film, CekimKosulu, Poz
from .forms import FilmForm, CekimKosuluForm, PozForm


def index(request):
    pozlar = Poz.objects.select_related('film', 'kosul').all()
    return render(request, 'shooting/index.html', {'pozlar': pozlar})


def film_create(request):
    if request.method == 'POST':
        form = FilmForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = FilmForm()
    return render(request, 'shooting/form.html', {'form': form})


def kosul_create(request):
    if request.method == 'POST':
        form = CekimKosuluForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CekimKosuluForm()
    return render(request, 'shooting/form.html', {'form': form})


def poz_create(request):
    if request.method == 'POST':
        form = PozForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PozForm()
    return render(request, 'shooting/form.html', {'form': form})
