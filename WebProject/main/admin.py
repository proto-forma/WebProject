from django.contrib import admin
from .models import *

modeli = [ Tvit, Tviteras, Lajk, Komentar ]

admin.site.register(modeli)
