from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views.generic import ListView
from django.urls import reverse_lazy
from django.core.mail import send_mail
from .forms import CandidaturaForm
from .models import Candidatura

class CandidaturaCreateView(FormView):
    template_name = 'candidaturas/candidatura_form.html'
    form_class = CandidaturaForm
    success_url = reverse_lazy('candidatura_sucesso')

    def form_valid(self, form):
        vaga = form.cleaned_data['vaga']
        nome = form.cleaned_data['nome']
        email = form.cleaned_data['email']
        curriculo = form.cleaned_data['curriculo']

        Candidatura.objects.create(
            vaga=vaga,
            nome=nome,
            email=email,
            curriculo=curriculo,
        )

        send_mail(
            f'Confirmação de candidatura à vaga: {vaga.titulo}',
            f'Olá {nome}, recebemos sua candidatura para a vaga {vaga.titulo}.',
            None,
            [email]
        )

        send_mail(
            f'Nova candidatura para {vaga.titulo}',
            f'Nome: {nome}/nEmail: {email}',
            None,
            ['teste@empregasenac.local']
        )

        return super().form_valid(form)
    

class CandidaturaListView(ListView):
    model = Candidatura
    template_name = "candidaturas/lista.html"
    context_object_name = "candidaturas"
