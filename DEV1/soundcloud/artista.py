from datetime import datetime

from genero import Genero

class Artista:
    """Documentaöao de artista, comtem seus atributos e metodos"""

    nome = str
    nome_artistico = str
    biografia = str
    seguidores = int
    nr_albums = int
    genero = Genero
    data_criacao = datetime
    nr_plays = int

    def __init__(self):
        """Documentacao"""

    def __str__(self):
        """Documentacao"""
        return 'String'

    def seguir(self):
        """Documentacao"""
        return 'boleano'
