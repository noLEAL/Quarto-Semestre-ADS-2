from datetime import datetime, time
from musica import Musica

class Playlist:
    """Documentaöao comtem catributos das playlist e seus metodos"""

    def __init__(self, titulo: str, descricao=None, duracao=None):
        """Documentacao"""
        self.titulo = titulo
        self.descricao = descricao
        self.data_cricao = datetime.now()
        self.nr_likes = 0
        self.duracao = duracao
        self.armazen = []

    def like(self):
        """Documentaöao"""

        self.nr_likes += 1

        return True

    def add_musica(self, musica: Musica):
        """Documentacao"""
        return "Boleano"

    def remove_musica(self, musica: Musica):
        """Documentacao"""
        return "Boleano"

    def __str__(self):
        """Documentacao"""

        to_string = f"=========================================================="
        to_string += f"\nTitulo:{self.titulo}  \nDescrição:{self.descricao}"
        to_string += f"\nData de Criação:{self.data_cricao} \nNumero de Likes:{self.nr_likes}"
        to_string += f"\nDuracao:{self.duracao} \nArmazen:{self.armazen}"
        to_string += f"\n=========================================================="

        return to_string
