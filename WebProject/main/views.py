from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from .models import *
from .form import *

# Create your views here.
def glavna_stranica(request):
    return render(request, 'base.html')

def naslovna (request):
    tviterasi = Tviteras.objects.exclude(korisnik=request.user)
    #if request.method == "POST":
        #form = TvitForm(request.POST or None)
        #if form.is_valid():
            #Tvit = form.save(commit=False)
            #Tvit.user = request.user
            #Tvit.save()
            #return redirect("tviter:naslovna_stranica")
    return render(request, 'main/naslovna.html', {'tviterasi': tviterasi})

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

def tviteras_list(request):
    tviterasi = Tviteras.objects.exclude(user=request.user)
    return render(request, 'main/tviteras_list.html', {'tviterasi': tviterasi})

def tvit(request, pk):
    tvit = Tvit.objects.get(pk=pk)
    if request.method == "POST":
        logirani_korisnik = request.user
        podaci = request.POST
        radnja_lajkanje = podaci.get("lajkanje")

        if radnja_lajkanje == "lajk":
            tvit.tvit_lajkovi.add(logirani_korisnik)
        elif radnja_lajkanje == "dislajk":
            tvit.tvit_lajkovi.remove(logirani_korisnik)

        tvit.save()
    return render(request, "main/tvit.html", {"tvit": tvit})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')

    else:
        form = UserCreationForm()

    context = {'form': form}

    return render(request, 'registration/register.html', context)