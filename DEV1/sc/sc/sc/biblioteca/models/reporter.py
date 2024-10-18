from django.db import models

class Reporter(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(null=True, blank=True)
    cpf = models.CharField(max_length=11)

    # relação com a classe person 1 / N

    def __str__(self):
        return "%s:%s:%s" % (self.name, self.email, self.cpf)