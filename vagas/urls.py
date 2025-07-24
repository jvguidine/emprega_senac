from django.urls import path
from .views import VagaCreateView, VagaListView
from django.views.generic import TemplateView

urlpatterns = [
    path('', VagaListView.as_view(), name='lista_vagas'),
    path('nova/', VagaCreateView.as_view(), name='nova_vaga'),
    path("sucesso/", TemplateView.as_view(template_name='vagas/sucesso.html'), name='vaga_sucesso'),
]