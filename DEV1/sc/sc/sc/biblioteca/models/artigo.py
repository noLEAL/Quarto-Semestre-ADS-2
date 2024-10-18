from django.db import models
from .reporter import Reporter

class Artigo(models.Model):
    titulo = models.CharField(max_length=100)
    publicado = models.DateField()
    reporter = models.ForeignKey(Reporter, on_delete=models.SET_NULL, null=True, blank=True)

#on_delete=models.SET_NULL - FOI DEFINIDO PARA QUE QUANDO O REPORTER FOR DELETADO AUTOMATICAMENTE IRA SETAR NULL
## relação com a classe person 1 / n
    def __str__(self):
        return self.titulo