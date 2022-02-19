from django.urls import path
from .views import glavna_stranica, tviteras

app_name = 'main'

urlpatterns = [
    path('', glavna_stranica, name='glavna_stranica'),
    path('tviteras/<int:pk>', tviteras, name='tviteras'),
]