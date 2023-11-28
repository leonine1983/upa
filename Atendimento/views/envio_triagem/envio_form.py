from Atendimento.models import envio_triagem, ficha_de_atendimento
from datetime import timezone, datetime, timedelta
from django.utils.safestring import mark_safe

from django import forms

class Envio_Form(forms.ModelForm):
    class Meta:
        model = envio_triagem
        fields = ['paciente_envio_triagem', 'retornou_em_menos_de_48_horas']

        widgets = {
            'paciente_envio_triagem': forms.Select(attrs={'class': 'form-control'}),
        }

    paciente_envio_triagem = forms.ModelMultipleChoiceField(
        queryset=ficha_de_atendimento.objects.all(),
    )
    retornou_em_menos_de_48_horas = forms.BooleanField(
        initial=False  # Define o valor inicial como False
    )
