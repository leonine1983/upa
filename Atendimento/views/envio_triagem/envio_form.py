"""from Atendimento.models import envio_triagem, ficha_de_atendimento
from datetime import timezone, datetime, timedelta
from django.utils.safestring import mark_safe

from django import forms


class Envio_Form(forms.ModelForm):
    class Meta:
        model = envio_triagem
        fields = ['paciente_envio_triagem', 'nome_acompanhante']

        widgets = {
            #'paciente_envio_triagem': forms.Select(attrs={'class': 'form-control'}),
            'nome_acompanhante':forms.TextInput(attrs={'class': 'form-control text-center '}),
        }
"""
from django import forms
from Atendimento.models import envio_triagem
import datetime

class Envio_Form(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(Envio_Form, self).__init__(*args, **kwargs)
        
        # Verifica se existem registros na base de dados
        if envio_triagem.objects.exists():
            # Obtém o último registro cadastrado
            ultimo_registro = envio_triagem.objects.latest('id')
            ultimo_codigo = ultimo_registro.cod_triagem
            novo_codigo = ""

            if ultimo_codigo is not None:
                # Se houver registro com cod_triagem
                ano, mes, sequencia = ultimo_codigo.split('-')
                ano_atual = str(datetime.datetime.now().year)[-2:]
                mes_atual = str(datetime.datetime.now().month).zfill(2)
                if ano != ano_atual:
                    novo_codigo = f"{ano_atual}-{mes_atual}-01"
                else:       
                    nova_sequencia = str(int(sequencia) + 1).zfill(len(sequencia))
                    novo_codigo = f"{ano_atual}-{mes_atual}-{nova_sequencia}"
                    self.initial['cod_triagem'] = novo_codigo
            else:
                ano_atual = str(datetime.datetime.now().year)[-2:]
                mes_atual = str(datetime.datetime.now().month).zfill(2)
                ultimo_codigo = f"{ano_atual}-{mes_atual}-3520"
                novo_codigo = ultimo_codigo
                self.initial['cod_triagem'] = novo_codigo
                return
        
    class Meta:
        model = envio_triagem
        fields = ['paciente_envio_triagem', 'nome_acompanhante', 'cod_triagem']

        widgets = {
            #'paciente_envio_triagem': forms.Select(attrs={'class': 'form-control'}),
            'nome_acompanhante': forms.TextInput(attrs={'class': 'form-control text-center'}),
            'cod_triagem': forms.TextInput(attrs={'class': 'form-control text-center'}),
        }
