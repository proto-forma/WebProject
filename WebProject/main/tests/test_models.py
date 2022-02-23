from datetime import datetime
from django.test import TestCase
from main.models import *


class Testmodels(TestCase):

    def setUp(self):
        self.tviteras1 = Tviteras.objects.create(
            ime = "neko-ime",
            lokacija = "TestCity",
            opis = "TestOpis",
            hendl = "TestHendl",
            vrijeme_pridruzivanja = datetime.now(),
        )
        self.tvit1 = Tvit.objects.create(
            stvorio_tvit = self.tviteras1.ime,
            tvit = "neki-tvit",
            
        )
        self.komentar1 = Komentar.objects.create(
            stvorio_kom = self.tviteras1.ime, 
            kom_na_tvit = self.tvit1.tvit,
            komentar = "neki-komentar",
        )
        self.lajk1 = Lajk.objects.create(
            stvorio_lajk = self.tviteras1.ime,
            lajkani_tvit = self.tvit1.tvit,
        )


    def test_tviteras(self):
        self.assertEquals(self.tviteras1.ime, "neko-ime")
        self.assertEquals(self.tviteras1.hendl, "TestHendl")
        self.assertEquals(self.tviteras1.opis, "TestOpis")
        self.assertEquals(self.tviteras1.lokacija, "TestCity")
        self.assertEquals(self.tviteras1.vrijeme_pridruzivanja)
        
    def test_tvit(self):
        self.assertEquals(self.tvit1.tijelo, "neki-tvit")
        self.assertEquals(self.tviteras1.ime, "neko-ime")
    
    def test_komentar(self):
        self.assertEquals(self.komentar1.tijelo, "neki-komentar")
        self.assertEquals(self.tviteras1.ime, "neko-ime")
        
    def test_tvit(self):
        self.assertEquals(self.tviteras1.stvorio, "neko-ime")
        self.assertEquals(self.tvit1.tvit, "neki-tvit")
        
