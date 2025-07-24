from django.db import models

# Create your models here.

NIVEIS = (
    ('estagio', 'Estágio'),
    ('junior', 'Júnior'),
    ('pleno', 'Pleno'),
    ('senior', 'Sênior'),
)

class Vaga(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    nivel = models.CharField(max_length=10, choices=NIVEIS)
    localidade = models.CharField(max_length=100)
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo