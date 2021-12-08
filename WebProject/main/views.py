from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homepage(request):
    kod = '<h1>Tviter</h1>'
    return HttpResponse(kod)