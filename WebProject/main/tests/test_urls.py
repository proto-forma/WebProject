from django.test import SimpleTestCase
from django.urls import reverse, resolve
from main.views import *


class TestUrls(SimpleTestCase):

    def test_glavna_str_url_is_resolved(self):
        url = reverse('glavna_stranica')

        self.assertEquals(resolve(url).func, glavna_stranica)

    def test_naslovna_url_is_resolved(self):
        url = reverse('naslovna_stranica')

        self.assertEquals(resolve(url).func, naslovna)

    def test_tviteras_url_is_resolved(self):
        url = reverse('tviteras', args=['1'])

        self.assertEquals(resolve(url).func, tviteras)

    def test_tvit_url_is_resolved(self):
        url = reverse('tvit', args=['1'])

        self.assertEquals(resolve(url).func, tvit)
    
    def test_novi_tviteras_url_is_resolved(self):
        url = reverse('novi_tviteras')

        self.assertEquals(resolve(url).func, novi_tviteras)
        
    def test_register_url_is_resolved(self):
        url = reverse('register')

        self.assertEquals(resolve(url).func, register)