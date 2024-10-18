from django.contrib import admin
from .models.exemplo import Exemplo
from .models.jogardor import Jogador
from .models.person import Person
from .models.passport import Passport
from .models.reporter import Reporter
from .models.artigo import Artigo
from .models.magazine import Magazine
from .models.papel import Papel

#admin.site.register(Exemplo)
#admin.site.register(Jogador)
#admin.site.register(Person)
#admin.site.register(Passport)
#admin.site.register(Reporter)
#admin.site.register(Artigo)
admin.site.register(Magazine)
admin.site.register(Papel)