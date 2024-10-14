from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Person(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nome Completo")
    birth_date = models.DateField(verbose_name="Data de nascimento")
    cpf = models.CharField(max_length=11, verbose_name="CPF", validators=[MinValueValidator(0)])