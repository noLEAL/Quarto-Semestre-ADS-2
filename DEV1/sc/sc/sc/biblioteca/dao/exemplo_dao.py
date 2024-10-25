from django.db.models import QuerySet
from biblioteca.dao.base import BaseManager


class ExemploDAO(BaseManager):

    def find_by_nome(self, nome: str) -> QuerySet['Exemplo']:
        if isinstance(nome, str):
            consulta = self.filter(nome__contains=nome)
            return consulta
        else:
            raise TypeError('Nome errado, sai daqui.')
