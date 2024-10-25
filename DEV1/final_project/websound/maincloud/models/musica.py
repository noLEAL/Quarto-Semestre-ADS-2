from django.core.validators import MinLengthValidator, MinValueValidator

from maincloud.models.base import BaseModel
from django.db import models
from maincloud.models.genero import Genero
from maincloud.models.artista import Artista
from maincloud.models.playlist import Playlist


class Musica(BaseModel):
    """
    Classe que representa uma música no sistema.

    Atributos:
        title (str): Título da música.
        leter (str): Letra da música.
        date_upload (date): Data de lançamento da música.
        nr_likes (int): Número de curtidas da música.
        duration (time): Duração da música.
        genre (str): Gênero musical da música.
        album (str): Nome do álbum da música.
        nr_plays (int): Número de reproduções da música.
        artista (ForeignKey): Referência ao artista responsável pela música.
        playlist (ManyToManyField): Referência às playlists que contêm a música.
    """

    title = models.CharField(max_length=100, validators=[MinLengthValidator(1)],verbose_name='Nome da Musica')
    leter = models.CharField(max_length=10000, validators=[MinLengthValidator(10)],blank=False, verbose_name='Letra da Musica' )
    date_upload = models.DateField(auto_now=True ,verbose_name='Data do Lançamento')
    nr_likes = models.IntegerField(default=0, validators=[MinValueValidator(0)], blank=False, verbose_name='Numero de likes')
    duration = models.TimeField(verbose_name='Duração da musica')
    genre = models.CharField(max_length=10, choices=[(tag.name, tag.value) for tag in Genero], verbose_name='Genero da Musica')
    album = models.CharField(max_length=100, validators=[MinLengthValidator(1)], verbose_name='Nome do Album')
    nr_plays = models.IntegerField(verbose_name='Numero de plays')
    artista = models.ForeignKey(Artista, on_delete=models.CASCADE, verbose_name='Artista responsavel')
    playlist = models.ManyToManyField(Playlist, verbose_name='Playlists')


    def __str__(self):
        """
        Retorna uma representação em string da música.

        Returns:
            str: Título da música.
        """
        return self.title

    class Meta:
        abstract = False