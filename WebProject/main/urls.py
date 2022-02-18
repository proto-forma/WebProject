from django.urls import path
from .views import *

urlpatterns = [
    path('', glavna_stranica, name='glavna_stranica'),
    #path('login.html/', login_str, name='login_stranica'),
]