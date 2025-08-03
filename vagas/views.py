from django.views.generic import ListView
from .models import Vaga, Candidatura
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from .forms import CandidaturaForm
from django.core.mail import send_mail
from django.contrib import messages



class VagaListView(ListView):
    model = Vaga
    template_name = 'vagas/lista.html'
    context_object_name = 'vagas'
    ordering = ['-data_criacao']

    def get_queryset(self):
        queryset = super().get_queryset()
        nivel = self.request.GET.get('nivel')
        localidade = self.request.GET.get('localidade')

        if nivel:
            queryset = queryset.filter(nivel__icontains=nivel)

        if localidade:
            queryset = queryset.filter(localidade__icontains=localidade)

        return queryset
from django.views.generic import DetailView

class VagaDetailView(DetailView):
    model = Vaga
    template_name = 'vagas/detalhe.html'
    context_object_name = 'vaga'

class CandidaturaCreateView(FormView):
    template_name = 'vagas/candidatura.html'
    form_class = CandidaturaForm
    success_url = reverse_lazy('lista_vagas')

    def get_initial(self):
        initial = super().get_initial()
        vaga_id = self.request.GET.get('vaga')
        if vaga_id:
            from .models import Vaga
            try:
                vaga = Vaga.objects.get(pk=vaga_id)
                initial['vaga'] = vaga
            except Vaga.DoesNotExist:
                pass
        return initial
    

    def form_valid(self, form):
        candidatura = Candidatura.objects.create(
            nome=form.cleaned_data['nome'],
            email=form.cleaned_data['email'],
            vaga=form.cleaned_data['vaga'],
            curriculo=form.cleaned_data['curriculo']
        )

        send_mail(
            subject='Confirmação de Candidatura',
            message=f'Olá {candidatura.nome}, sua candidatura para a vaga "{candidatura.vaga.titulo}" foi recebida com sucesso!',
            from_email=None,
            recipient_list=[candidatura.email]
        )

        send_mail(
            subject='Nova Candidatura Recebida',
            message=f'{candidatura.nome} se candidatou à vaga "{candidatura.vaga.titulo}".',
            from_email=None,
            recipient_list=['rh@empresa.com']
        )
        
        messages.success(self.request, 'Candidatura enviada com sucesso!')
        return super().form_valid(form)



    def form_valid(self, form):
        Candidatura.objects.create(
            nome=form.cleaned_data['nome'],
            email=form.cleaned_data['email'],
            vaga=form.cleaned_data['vaga'],
            curriculo=form.cleaned_data['curriculo']
        )
        return super().form_valid(form)
