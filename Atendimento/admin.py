from django.contrib import admin
from .models import genero_sexual, ficha_de_atendimento, envio_triagem

# Register your models here.
admin.site.register(genero_sexual),
admin.site.register(ficha_de_atendimento),
admin.site.register(envio_triagem)