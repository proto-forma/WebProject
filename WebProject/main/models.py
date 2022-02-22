from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

class Tvit(models.Model):
    tijelo = models.CharField(max_length=255)
    stvorio = models.ForeignKey(User, related_name='tvitovi', on_delete=models.CASCADE)
    vrijeme_stvaranja = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-vrijeme_stvaranja',)

    def __str__(self):
            return "{} ({}): {}".format(self.stvorio.username, self.vrijeme_stvaranja, self.tijelo[:30])

class Tviteras(models.Model):
    korisnik = models.OneToOneField(User, on_delete=models.CASCADE)
    ime = models.CharField(max_length=50)
    hendl = models.CharField(max_length=50)
    opis = models.CharField(max_length=255)
    lokacija = models.CharField(max_length=50)
    datum_pridruzivanja = models.DateField(auto_now_add=True)
    prati = models.ManyToManyField('self', related_name='pracen_od', symmetrical=False, blank=True)
    #avatar = models.ImageField(upload_to='uploads/', blank=True, null=True)

    def __str__(self):
        return "{} ({})".format(self.hendl, self.id, self.korisnik.username)



class Lajk(models.Model):
    tvit = models.ForeignKey(Tvit, related_name='lajkovi', on_delete=models.CASCADE)
    stvorio = models.ForeignKey(User, related_name='lajkovi', on_delete=models.CASCADE)
    vrijeme_lajkanja = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return "({1}) {0}".format(self.tvit.tijelo, self.id)

class Komentar(models.Model):
    tijelo = models.CharField(max_length=255)
    tvit = models.ForeignKey(Tvit, related_name='komentari', on_delete=models.CASCADE)
    stvorio = models.ForeignKey(User, related_name='komentari', on_delete=models.CASCADE)
    vrijeme_komentiranja = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ('-vrijeme_komentiranja',)

    def __str__(self):
        return "{} (tvit {}) {}".format(self.stvorio.username, self.tvit.id, self.tijelo)


