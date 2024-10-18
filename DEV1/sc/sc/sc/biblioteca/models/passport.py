from django.db import models
from datetime import datetime
from .person import Person
from django.core.validators import MaxValueValidator, MinValueValidator

class Passport(models.Model):
    number = models.CharField(max_length=10, verbose_name="Passaport Number")
    issue_date = models.DateField(verbose_name="Data de Criação")
    expiration_date = models.DateField(verbose_name="Data de Vencimento")
    owner = models.OneToOneField(Person, on_delete=models.CASCADE, primary_key=True)

# relação com a classe person 1 / 1