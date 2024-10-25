import datetime
import random
from faker import Faker
from maincloud.models.artista import Artista
from maincloud.models.musica import Musica
from maincloud.models.playlist import Playlist
from maincloud.models.genero import Genero
from django.contrib.auth import get_user_model


falso = Faker('pt_BR')

# User = get_user_model()
# User.objects.create_superuser('admin', 'admin@myproject.com', 'admin')
# # Criar superusuário

#
# # Função para criar artistas
# def create_artists(n=10):
#     for _ in range(n):
#         artist = Artista(
#             name=falso.name(),
#             artistic_name=falso.sentence(nb_words=2),
#             biography=falso.text(max_nb_chars=200),
#             follower=random.randint(0, 10000),
#             nr_album=random.randint(1, 20),
#             genre=random.choice([tag.name for tag in Genero]),
#             nr_plays=random.randint(0, 100000)
#         )
#         artist.full_clean()
#         artist.save()

# # Função para criar músicas
def create_musics(n=10):
    for _ in range(n):
        duration_seconds = random.randint(60, 300)
        duration = datetime.time(duration_seconds // 3600, (duration_seconds % 3600) // 60, duration_seconds % 60)
        music = Musica(
            title=falso.sentence(nb_words=3),
            leter=falso.text(350),
            nr_likes=random.randint(1,10000),
            duration=duration,
            genre=random.choice([tag.name for tag in Genero]),
            album=falso.sentence(nb_words=2),
            nr_plays=random.randint(1,10000),
            artista=Artista.objects.order_by('?').first(),
        )
        music.full_clean()
        music.save()
        playlists = Playlist.objects.order_by('?')[:random.randint(1, 19)]
        music.playlist.set(playlists)

#Função para criar playlists
# def create_playlists(n=10):
#     for _ in range(n):
#         duration_seconds = random.randint(60, 300)
#         duration = datetime.time(duration_seconds // 3600, (duration_seconds % 3600) // 60, duration_seconds % 60)
#         playlist = Playlist(
#             title=falso.sentence(nb_words=2),
#             description=falso.text(max_nb_chars=300),
#             nr_likes=random.randint(1,10000),
#             duration=duration
#         )
#         playlist.full_clean()
#         playlist.save()

# Gerar dados
#create_artists(10)
create_musics(10)
#create_playlists(10)
