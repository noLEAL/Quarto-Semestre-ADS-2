from datetime import time, datetime
from genero import Genero


class Musica:
    """Documentaöäao da  classe de Musica, Contem metodos e caracteristicas das musicas """


    def __init__(self, titulo: str, data_upload: str, duracao: str, genero: Genero, album: str, letra=None):
        """Documentação"""
        formatime = "%H:%M:%S"
        formatdate = "%d/%m/%Y"
        self.titulo = titulo
        self.data_upload = datetime.strptime(data_upload,formatdate)
        self.nr_likes = 0
        self.duracao = time.strptime(duracao, formatime)
        self.genero = genero
        self.album = album
        self.nr_plays = 0
        self.letra = letra


    def like(self):

        self.nr_likes += 1

        return True

    def play(self):

        self.nr_plays += 1

        return True

    def __str__(self):
        """Documentação"""

        to_string = f"=========================================================="
        to_string += f"\nTitulo:{self.titulo}  \nLetra:{self.letra}"
        to_string += f"\nData de Criação:{self.data_upload} \nNumero de Likes:{self.nr_likes}"
        to_string += f"\nDuracao:{self.duracao} \nGenero:{self.genero}"
        to_string += f"\nAlbum:{self.album} \nNumero de Plays:{self.nr_plays}"
        to_string += f"\n=========================================================="

        return to_string