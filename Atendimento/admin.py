from django.contrib import admin
from .models import genero_sexual, ficha_de_atendimento, envio_triagem, Bairro, Bairro_Vera_Cruz, Rua, Cidade, Estado, Pais

# Register your models here.
admin.site.register(genero_sexual),
admin.site.register(ficha_de_atendimento),
admin.site.register(envio_triagem)
admin.site.register(Bairro)
admin.site.register(Bairro_Vera_Cruz)
admin.site.register(Rua)
admin.site.register(Cidade)
admin.site.register(Estado)
admin.site.register(Pais)