from django import forms
from .models import *

class TvitForm(forms.ModelForm):
    tijelo = forms.CharField(
        required=True,
        widget=forms.widgets.Textarea(
            attrs={
                "placeholder": "Šta je tvoje danas, to je sutra moje, lave...",
                "class": "input is-grey-light is-medium",
            }
        ),
        label="",
    )

    class Meta:
        model = Tvit
        exclude = ("stvorio", "tvit_lajkovi", "tvit_komentari", )


class KomentarForm(forms.ModelForm):
    tijelo = forms.CharField(
        widget=forms.widgets.Textarea(
            attrs={
                "placeholder": "Članak lomi čeljust, kolino ti slomi rame...",
                "class": "input is-grey-light is-medium",
            }
        ),
        label="",
    )

    class Meta:
        model = Komentar
        exclude = ("stvorio", "tvit", )


class TviterasForm(forms.ModelForm):
    ime = forms.CharField(
        widget=forms.widgets.Textarea(
            attrs={
                "placeholder": "Grše",
                "class": "input is-grey-light is-medium",
            }
        ),
        label="Ime",
    ) 

    hendl = forms.CharField(
        widget=forms.widgets.Textarea(
            attrs={
                "placeholder": "grše69",
                "class": "input is-grey-light is-medium",
            }
        ),
        label="Hendl",
    )

    opis = forms.CharField(
        widget=forms.widgets.Textarea(
            attrs={
                "placeholder": "Palme, high sky, more, night ride...",
                "class": "input is-grey-light is-medium",
            }
        ),
        label="Opis",
    )

    lokacija = forms.CharField(
        widget=forms.widgets.Textarea(
            attrs={
                "placeholder": "Split",
                "class": "input is-grey-light is-medium",
            }
        ),
        label="Lokacija",
    )

    class Meta:
        model = Tviteras
        exclude = ("korisnik", "prati", )