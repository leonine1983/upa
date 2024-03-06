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
        else:
            # Se não houver registros na base de dados, define o código inicial para o mês atual
            ano_atual = str(datetime.datetime.now().year)
            mes_atual = str(datetime.datetime.now().month).zfill(2)
            novo_codigo = f"{ano_atual}-{mes_atual}-01"
            self.initial['cod_triagem'] = novo_codigo
            return  # Interrompe a execução do método __init__

        # Se houver registros, continue com o código para obter o novo código
        ano, mes, sequencia = ultimo_codigo.split('-')
        
        # Verifica se o ano e mês atual são diferentes dos do último registro
        ano_atual = str(datetime.datetime.now().year)
        mes_atual = str(datetime.datetime.now().month).zfill(2)
        if ano != ano_atual or mes != mes_atual:
            # Se for diferente, atualiza o ano e mês atual e redefine a sequência para '01'
            novo_codigo = f"{ano_atual}-{mes_atual}-01"
        else:
            # Caso contrário, incrementa a sequência em 1
            nova_sequencia = str(int(sequencia) + 1).zfill(len(sequencia))
            novo_codigo = f"{ano_atual}-{mes_atual}-{nova_sequencia}"
        
        # Define o valor inicial do campo cod_triagem
        self.initial['cod_triagem'] = novo_codigo

    class Meta:
        model = envio_triagem
        fields = ['paciente_envio_triagem', 'nome_acompanhante', 'cod_triagem']

        widgets = {
            #'paciente_envio_triagem': forms.Select(attrs={'class': 'form-control'}),
            'nome_acompanhante': forms.TextInput(attrs={'class': 'form-control text-center'}),
        }
