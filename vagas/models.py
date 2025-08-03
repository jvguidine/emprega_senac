from django.db import models

class Vaga(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    nivel = models.CharField(max_length=50)
    localidade = models.CharField(max_length=100)
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    empresa = models.CharField(max_length=100)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

class Candidatura(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    vaga = models.ForeignKey(Vaga, on_delete=models.CASCADE)
    curriculo = models.FileField(upload_to='curriculos/')
    data_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nome} - {self.vaga.titulo}"
