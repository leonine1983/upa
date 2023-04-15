from django.contrib import admin
from .models import Classifica_risco_model, triagem, CustomUserTriagem

# Register your models here.

admin.site.register(Classifica_risco_model),
admin.site.register(triagem)
admin.site.register(CustomUserTriagem)