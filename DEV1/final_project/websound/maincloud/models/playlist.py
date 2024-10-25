from django.core.validators import MinLengthValidator

from maincloud.models.base import BaseModel
from django.db import models

class Playlist(BaseModel):
    """
    Classe que representa uma playlist no sistema.

    Atributos:
        title (str): Nome da playlist.
        description (str): Descrição da playlist.
        create_date (date): Data de criação da playlist.
        nr_likes (int): Número de curtidas da playlist.
        duration (time): Tempo total da playlist.
    """

    title = models.CharField(max_length=100, validators=[MinLengthValidator(1)], verbose_name='Nome da Playlist')
    description = models.CharField(max_length=500, validators=[MinLengthValidator(10)], blank=False, verbose_name='Descrição da playlist')
    create_date = models.DateField(auto_now=True, verbose_name='Data de Criação')
    nr_likes = models.IntegerField(default=0, blank=False, verbose_name='Numero de likes')
    duration = models.TimeField(verbose_name='Tempo total da playlist')

    class Meta:
        abstract = False

    def __str__(self):
        """
        Retorna uma representação em string da playlist.

        Returns:
            str: Título da playlist.
        """
        return self.title