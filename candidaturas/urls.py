from django.urls import path
from django.views.generic import TemplateView
from .views import CandidaturaCreateView, CandidaturaListView

urlpatterns = [
    path('nova/', CandidaturaCreateView.as_view(), name='candidatar'),
    path('lista/', CandidaturaListView.as_view(), name='lista_candidaturas'),
    path('sucesso/', TemplateView.as_view(template_name='candidaturas/sucesso.html'), name='candidatura_sucesso'),
]