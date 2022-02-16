from django.contrib import admin
from django.contrib.auth.models import Group
from .models import *

modeli = [ Tvit, Tviteras, Lajk, Komentar ]

admin.site.unregister(Group)
admin.site.register(modeli)
