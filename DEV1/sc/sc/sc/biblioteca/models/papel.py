from django.db import models
from .magazine import Magazine

class Papel(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateField()
    magazine = models.ManyToManyField(Magazine)

    def __str__(self):
        return self.title

