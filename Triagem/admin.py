from django.contrib import admin
from .models import Classifica_risco_model, triagem, CustomUserTriagem, Exames_Model, Tipos_Atendimento,Atendimento_especializado

# Register your models here.

admin.site.register(Classifica_risco_model),
admin.site.register(triagem),
admin.site.register(CustomUserTriagem),
admin.site.register(Exames_Model),
admin.site.register(Tipos_Atendimento),
admin.site.register(Atendimento_especializado)