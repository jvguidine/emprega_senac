from django.db import models
from vagas.models import Vaga

class Candidatura(models.Model):
    vaga = models.ForeignKey(Vaga, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    curriculo = models.FileField(upload_to='curriculos/')
    data_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.nome} - {self.vaga.titulo}'