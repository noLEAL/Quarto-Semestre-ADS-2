from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime

class Jogador(models.Model):
    """Documentação """

    nome = models.CharField(max_length=100)
    apelido = models.CharField(max_length=50, blank=True)
    data_nascimento = models.DateTimeField()
    numero = models.IntegerField(validators=[MinValueValidator(1)])
    posicao = models.CharField(max_length=20)
    qualidade = models.IntegerField(validators=[
        MinValueValidator(1),
        MaxValueValidator(100)
    ])
    cartoes = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    suspenso = models.BooleanField(default=False)


    def __str__(self):
        return (f"Nome: {self.nome}, Apelido: {self.apelido}, "
                f"Data de Nascimento: {self.data_nascimento}, Número: {self.numero}, "
                f"Posição: {self.posicao}, Qualidade: {self.qualidade}, "
                f"Cartões: {self.cartoes}, Suspenso: {self.suspenso}")

    @property
    def idade(self):
        return (datetime.now() - self.data_nascimento).days // 365

    class Meta:
        verbose_name_plural = "Jogadores"