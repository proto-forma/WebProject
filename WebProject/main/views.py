from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from .models import *
from .form import *
from django.contrib.auth.decorators import login_required

# Create your views here.
def glavna_stranica(request):
    return render(request, 'base.html')


@login_required
def naslovna(request):
    tviterasi = Tviteras.objects.exclude(korisnik=request.user)
    trenutni_path = request.path
    form = TvitForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            Tvit = form.save(commit=False)
            Tvit.stvorio = request.user
            Tvit.save()
            return redirect(trenutni_path)
    return render(request, 'main/naslovna.html', {'tviterasi': tviterasi, 'form': form})


@login_required
def tviteras_list(request):
    tviterasi = Tviteras.objects.exclude(user=request.user)
    return render(request, 'main/tviteras_list.html', {'tviterasi': tviterasi})


@login_required
def tviteras(request, pk):
    tviteras = Tviteras.objects.get(pk=pk)
    if request.method == "POST":
        logirani_tviteras = request.user.tviteras
        podaci = request.POST
        radnja_pracenje = podaci.get("pracenje")

        if radnja_pracenje == "zaprati":
            logirani_tviteras.prati.add(tviteras)
        elif radnja_pracenje == "otprati":
            logirani_tviteras.prati.remove(tviteras)

        logirani_tviteras.save()
    return render(request, "main/tviteras.html", {"tviteras": tviteras})


@login_required
def tvit(request, pk):
    tvit = Tvit.objects.get(pk=pk)
    trenutni_path = request.path
    form = KomentarForm(request.POST or None)

    if request.method == "POST":
        
        if form.is_valid():
            komentar = form.save(commit=False)
            komentar.tvit = tvit
            komentar.stvorio = request.user
            komentar.save()
            return redirect(trenutni_path)

        logirani_korisnik = request.user
        podaci = request.POST
        radnja_lajkanje = podaci.get("lajkanje")

        if radnja_lajkanje == "lajk":
            tvit.tvit_lajkovi.add(logirani_korisnik)
        elif radnja_lajkanje == "dislajk":
            tvit.tvit_lajkovi.remove(logirani_korisnik)

        tvit.save()
        return redirect(trenutni_path)

    return render(request, "main/tvit.html", {"tvit": tvit, "form": form})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('main:uredi_tviterasa')
    else:
        form = UserCreationForm()

    context = {'form': form}

    return render(request, "registration/register.html", context)

@login_required
def uredi_tviterasa(request):
    tviteras = request.user.tviteras
    form = TviterasForm(request.POST or None, instance=tviteras)

    if request.method == "POST":
        if form.is_valid():
            novi_podaci = form.save(commit=False)
            novi_podaci.save()

            return redirect('main:naslovna_stranica')

    return render(request, "main/uredi_tviterasa.html", {"form": form})
