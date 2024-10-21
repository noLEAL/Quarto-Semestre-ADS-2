from django.contrib.auth.password_validation import MinimumLengthValidator

from .base import *
from django.db import models

class Exemplo(models.Model):

    cod = models.CharField(max_length=10,  validators=[MinimumLengthValidator(10)], blank=True)
    nome = models.CharField(max_length=15,  validators=[MinimumLengthValidator(3)])

    object = ExemploDAO()

def __str__(self):
    return 'deu certo '
