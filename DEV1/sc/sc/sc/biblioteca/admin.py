from django.contrib import admin
from .models.exemplo import Exemplo
from .models.jogardor import Jogador
from .models.person import Person
from .models.passport import Passport

admin.site.register(Exemplo)
admin.site.register(Jogador)
admin.site.register(Person)
admin.site.register(Passport)