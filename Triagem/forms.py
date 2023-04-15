from datetime import date

from django import forms

from Atendimento.models import envio_triagem

from .models import triagem


class TriagemEnfermariaForm(forms.ModelForm):
    data_hoje = date.today()
    paciente_triagem = forms.ModelChoiceField( label='Paciente aguardando a triagem', queryset=envio_triagem.objects.filter(data_envio_triagem=data_hoje).exclude(triagem_concluida=1))
    

    class Meta:
        model = triagem
        fields = ['paciente_triagem', 'frequencia_cardiaca_FC', 'pressao_arterial_PA', 'frequencia_respiratoria_FR',
                  'saturacao_de_oxigenio_SPO2', 'hemoglicoteste_HGT', 'temperatura_TEMP', 'peso', 'classifica_tipo',
                  'observacao']
        labels = {
            'observacao': 'Sitomas relatados pelo paciente'
        }

        widgets = {
            'observacao': forms.Textarea(attrs={'rows': 6}),
        }
       


