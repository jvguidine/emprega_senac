from django import forms
from vagas.models import Vaga

class CandidaturaForm(forms.Form):
    nome = forms.CharField(max_length=100, label='Seu nome')
    email = forms.EmailField(label='Seu e-mail')
    vaga = forms.ModelChoiceField(queryset=Vaga.objects.all(), label='Selecione a vaga')
    curriculo = forms.FileField(label='Currículo (PDF)')

    def clean_curriculo(self):
        arquivo = self.cleaned_data['curriculo']
        if not arquivo.name.lower().endswith('.pdf'):
            raise forms.ValidationError('Envie um arquivo PDF válido.')
        return arquivo 