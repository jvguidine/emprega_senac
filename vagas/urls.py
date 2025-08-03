from django.urls import path
from .views import VagaListView, VagaDetailView, CandidaturaCreateView

urlpatterns = [
    path('', VagaListView.as_view(), name='lista_vagas'),
    path('vaga/<int:pk>/', VagaDetailView.as_view(), name='detalhe_vaga'),
    path('candidatura/', CandidaturaCreateView.as_view(), name='candidatar'),
]
