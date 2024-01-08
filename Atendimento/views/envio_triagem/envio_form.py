from Atendimento.models import envio_triagem, ficha_de_atendimento
from datetime import timezone, datetime, timedelta
from django.utils.safestring import mark_safe

from django import forms


class Envio_Form(forms.ModelForm):
    class Meta:
        model = envio_triagem
        fields = ['paciente_envio_triagem', 'nome_acompanhante', 'retornou_em_menos_de_48_horas']

        widgets = {
            #'paciente_envio_triagem': forms.Select(attrs={'class': 'form-control'}),
            'nome_acompanhante':forms.TextInput(attrs={'class': 'form-control text-center '}),
        }
