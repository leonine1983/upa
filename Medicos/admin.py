from django.contrib import admin
from .models import Medico_atendimento, CustomUser, CadastroSala, Salas_Atendimento, cid_10

# Register your models here.
admin.site.register(Medico_atendimento)
admin.site.register(CustomUser)
admin.site.register(CadastroSala)
admin.site.register(Salas_Atendimento)
admin.site.register(cid_10)
