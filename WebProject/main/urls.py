from django.urls import path
from .views import glavna_stranica

urlpatterns = [
    path('', glavna_stranica, name='glavna_stranica'),
]