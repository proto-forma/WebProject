from django.urls import path
from .views import *

app_name = 'main'

urlpatterns = [
    path('', glavna_stranica, name='glavna_stranica'),
    path('naslovna/', naslovna, name='naslovna_stranica'),
    path('tviteras/<int:pk>', tviteras, name='tviteras'),
]