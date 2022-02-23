from django.test import TestCase, Client
from django.urls import reverse
from main.models import *
import datetime


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.glavna_stranica_url = reverse('glavna_stranica')
        self.tviteras_url = reverse('tviteras', args=['1'])
        self.naslovna_url = reverse('naslovna_stranica')
        self.tvit_url = reverse('tvit', args=["1"])
        self.tviteras_list_url = reverse('homepage')

        self.tviteras1 = Tviteras.objects.create(
            ime = "neko-ime",
            lokacija = "TestCity",
            opis = "TestOpis",
            hendl = "TestHendl",
            vrijeme_pridruzivanja = datetime.now(),
        )
            

    def test_project_glavna_stranica_GET(self):

        response = self.client.get(self.glavna_stranica_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')

    def test_project_naslovna_GET(self):

        response = self.client.get(self.naslovna_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/naslovna.html')
        
    def test_project_tvit_GET(self):

        response = self.client.get(self.tvit_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/tvit.html')
        
    def test_project_tviteras_GET(self):
        
        response = self.client.get(self.tviteras_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/tviteras.html')
        
    def test_project_tviteras_list_GET(self):

        response = self.client.get(self.tviteras_list_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/tviteras_list.html')