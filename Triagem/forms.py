from datetime import date
from django import forms
from Atendimento.models import envio_triagem, ficha_de_atendimento

from .models import triagem, Classifica_risco_model

# CADASTRA O ID DO PACIENTE NA TRIAGEM
class TriagemEnfermariaForm(forms.ModelForm):
    data_hoje = date.today()
    paciente_triagem = forms.ModelChoiceField( label='Paciente aguardando ser chamado para a CLASSIFICAÇÃO', queryset=envio_triagem.objects.filter(data_envio_triagem=data_hoje).exclude(triagem_concluida=1))    

    class Meta:
        model = triagem
        fields = ['paciente_triagem']  


# Recebe o Id da view 'triagem_enfermaria' e busca o restante dos campos para serem preenchidos
class TriagemEnfermariaUpdateForm(forms.ModelForm):
    class Meta:
        model = triagem
        fields = ['frequencia_cardiaca_FC', 'pressao_arterial_PA_2', 'pressao_arterial_PA', 'frequencia_respiratoria_FR',
                  'saturacao_de_oxigenio_SPO2', 'hemoglicoteste_HGT', 'temperatura_TEMP', 'peso', 'altura',
                  'observacao']
        labels = {
            'observacao': 'Sintomas relatados pelo paciente',
        }

        widgets = {
            'observacao': forms.Textarea(attrs={'rows': 6}),
        }

    def __init__(self, *args, **kwargs):
        super(TriagemEnfermariaUpdateForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = True

    
class TriagemEnfermaria_Alergias_UpdateForm(forms.ModelForm):   
     
    conteudo_alergia = forms.CharField(required=False)

    class Meta:
        model = ficha_de_atendimento
        fields = [ 'alergias', 'conteudo_alergia', 'comorbidades', 'conteudo_comorbidades' ]
        labels = {
            'alergias' : 'O paciente possui algum tipo de alergia?',
            'conteudo_alergia': 'Descreva a alergia do paciente'
        }

        widgets = {
            'conteudo_alergia': forms.Textarea(attrs={
                 'rows': 100,
                 'cols':500,
                 }),
            
        }       


class Classifica_form(forms.ModelForm):

    classifica_tipo = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'border border-info p-2 pb-1 bg-transparent text-info col m-2 rounded-1'}),
    )
    descri = forms.CharField(
        widget = forms.Textarea(attrs={'class': 'border border-info p-2 pb-1 bg-transparent text-info col m-2 rounded-1'}),
        required=False          
    )     

    class Meta:
        model = Classifica_risco_model
        fields = '__all__'
    


