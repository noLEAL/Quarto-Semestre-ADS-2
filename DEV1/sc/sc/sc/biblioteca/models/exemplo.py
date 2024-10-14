from .base import *
from django.db import models

class Exemplo(models.Model):
    titulo = models.CharField(max_length=10)

def __str__(self):
    return 'deu certo '
