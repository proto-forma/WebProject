from django import forms
from .models import *

class TvitForm(forms.ModelForm):
    body = forms.CharField(
        required=True,
        widget=forms.widgets.Textarea(
            attrs={
                "placeholder": "Tvit tvit tvit...",
                "class": "textarea is-success is-medium",
            }
        ),
        label="",
    )

    class Meta:
        model = Tvit
        exclude = ("stvorio", )

class KomentarForm(forms.ModelForm):
    tijelo = forms.CharField(
        widget=forms.widgets.Textarea(
            attrs={
                "placeholder": "Tvit tvit tvi...",
                "class": "input is-grey-light is-medium",
            }
        ),
        label="",
    )

    class Meta:
        model = Komentar
        exclude = ("stvorio", "tvit", )