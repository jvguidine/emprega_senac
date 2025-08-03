from django import forms
from .models import Vaga

class CandidaturaForm(forms.Form):
    nome = forms.CharField(max_length=100)
    email = forms.EmailField()
    vaga = forms.ModelChoiceField(queryset=Vaga.objects.all(), widget=forms.HiddenInput())
    curriculo = forms.FileField()
