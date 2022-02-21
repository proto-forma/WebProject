from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from .models import *

# Create your views here.
def glavna_stranica(request):
    return render(request, 'base.html')
def naslovna (request):
    
    return render(request, 'main/naslovna.html')

def tviteras(request, pk):
    tviteras = Tviteras.objects.get(pk=pk)
    if request.method == "POST":
        trenutni_tviteras = request.user.tviteras
        data = request.POST
        action = data.get("follow")
        if action == "follow":
            trenutni_tviteras.prati.add(tviteras)
        elif action == "unfollow":
            trenutni_tviteras.prati.remove(tviteras)
        trenutni_tviteras.save()
    return render(request, "main/tviteras.html", {"tviteras": tviteras})

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