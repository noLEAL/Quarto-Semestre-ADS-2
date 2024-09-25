from datetime import datetime, time
from musica import Musica
from exterminador import Exterminador


class Playlist:
    """Documentaöao comtem catributos das playlist e seus metodos"""

    titulo = str
    descricao = str
    data_cricao = datetime
    nr_likes = int
    duracao = time

    def __init__(self, titulo: str):
        """Documentacao"""
        self.titulo = titulo

    def like(self):
        """Documentaöao"""
        return "boleano"

    def add_musica(self, musica: Musica):
        """Documentacao"""
        return "Boleano"

    def remove_musica(self, musica: Musica):
        """Documentacao"""
        return "Boleano"

    def __str__(self):
        """Documentacao"""

        return print("Titulo:", self.titulo)
