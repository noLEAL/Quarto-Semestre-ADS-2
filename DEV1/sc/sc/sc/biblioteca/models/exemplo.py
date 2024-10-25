import string
import random
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models
from reportlab.lib.pagesizes import letter
from ..dao.exemplo_dao import ExemploDAO
from .base import BaseModel
from .validators import CodValidator


class Exemplo(BaseModel):

    cod = models.CharField(max_length=10,  validators=[MinLengthValidator(10), CodValidator], blank=True)
    nome = models.CharField(max_length=15,  validators=[MinLengthValidator(3)], default='sem nome')

    object = ExemploDAO()

    #"" string pode ser alterada aqualquer momento
    #'' string constante, idealmente não seria mutavel

    def save(self, *args, **kwargs):
        if self.cod is None or self.cod == '':
            letters = string.ascii_letters + string.digits
            self.cod = ''.join(random.choice(letters) for i in range(10))
        super().save(*args, **kwargs)

    def clean(self):
        if not  isinstance(str(self.nome), str):
            raise ValidationError({"nome": 'Nome informado é do tipo errado'},code="error001")
        elif self.nome == "Teste":
            raise ValidationError({"nome": 'Não é possivel slavar teste'},code="erros 002")
        elif self.cod == "1111111111" and self.nome == "IFRS restinga":
            raise ValidationError({"nome": 'Combinação de nome e codigo errado!'},code="Error0101")

    def __str__(self):
        return self.nome
