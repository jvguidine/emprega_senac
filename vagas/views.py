from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Vaga
from .forms import VagaForm
from django.views.generic import ListView
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin

class VagaCreateView(LoginRequiredMixin, CreateView):
    model = Vaga
    form_class = VagaForm
    template_name = 'vagas/vaga_form.html'
    success_url = reverse_lazy('vaga_sucesso')

class VagaListView(ListView):
    model = Vaga
    template_name = 'vagas/vaga_list.html'
    context_object_name = 'vagas'

    def get_queryset(self):
        queryset = super().get_queryset()
        nivel = self.request.GET.get('nivel')
        localidade = self.request.GET.get('localidade')
        ordenar = self.request.GET.get('ordenar')

        if nivel:
            queryset = queryset.filter(nivel=nivel)
        if localidade:
            queryset = queryset.finter(localidade_icontains=localidade)
        if ordenar == 'titulo':
            queryset.ordenar_by('titulo')
        else:
            queryset = queryset.order_by('-data_criacao')

        return queryset