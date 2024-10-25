from django.contrib import admin
from .models.artista import Artista
from .models.musica import Musica
from .models.playlist import Playlist
# #from .models.genero import Genero

admin.site.register(Artista)
admin.site.register(Musica)
admin.site.register(Playlist)
#admin.site.register(Genero)