from django.core.validators import MinLengthValidator
from maincloud.models.genero import Genero
from maincloud.models.base import BaseModel
from django.db import models

class Artista(BaseModel):
    """
    Classe que representa um artista no sistema.

    Atributos:
        name (str): Nome do artista.
        artistic_name (str): Nome artístico do artista.
        biography (str): Biografia do artista.
        follower (int): Número de seguidores do artista.
        nr_album (int): Quantidade de álbuns do artista.
        genre (str): Gênero musical do artista.
        creation_date (date): Data de criação do registro do artista.
        nr_plays (int): Número de reproduções das músicas do artista.
    """

    name = models.CharField(max_length = 100, validators=[MinLengthValidator(5)], verbose_name='Nome do Artista')
    artistic_name = models.CharField(max_length=50, validators=[MinLengthValidator(1)], verbose_name='Nome Artistico')
    biography = models.CharField(max_length=500, validators=[MinLengthValidator(0)], verbose_name='Biografia do Artista', blank=False)
    follower = models.IntegerField(default=0, blank=False, verbose_name='Número de Seguidores')
    nr_album = models.IntegerField(default=1, verbose_name='Quantidade de Albuns')
    genre = models.CharField(max_length=10, choices=[(tag.name, tag.value) for tag in Genero], verbose_name='Genero')
    creation_date = models.DateField(auto_now=True, verbose_name='Data de Criação')
    nr_plays = models.IntegerField()



    def __str__(self):
        """
        Retorna uma representação em string do artista.

        Returns:
            str: Nome do artista.
        """

        # to_string = f"Nome: {self.name}, Nome Artístico: {self.artistic_name}, Biografia: {self.biography}/n"
        # to_string += f"Seguidores: {self.follower}, Número de Álbuns: {self.nr_album}, Gênero: {self.genre}"
        # to_string += f"Data de Criação: {self.creation_date}, Número de Plays: {self.nr_plays}"


        return  self.name


    class Meta:
        abstract = False