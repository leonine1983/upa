from django.contrib import admin
from .models import config_Marquee, Video_Backgroud_Painel, Notificate_system
from Atendimento.models import Licenca

# Register your models here
admin.site.register(Licenca)
admin.site.register(config_Marquee)
admin.site.register(Video_Backgroud_Painel)
admin.site.register(Notificate_system)

