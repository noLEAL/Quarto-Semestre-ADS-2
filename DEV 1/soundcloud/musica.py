from datetime import datetime, time
from genero import Genero


class Musica:
    """Documentaöäao da  classe de Musica, Contem metodos e caracteristicas das musicas """

    titulo = str
    letra = str
    data_upload = datetime
    nr_likes = int
    duracao = time
    genero = Genero
    album = str
    nr_plays = int

    def __init__(self):
        """Documentação"""

    def like(self):
        return "boleano"

    def play(self):
        return "boleano"

    def __str__(self):
        """Documentação"""
        return "String"