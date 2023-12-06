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
#class TriagemEnfermariaUpdateForm(forms.ModelForm):
 #   class Meta:
  #      model = triagem
   #     fields = ['frequencia_cardiaca_FC', 'pressao_arterial_PA_2', 'pressao_arterial_PA', 'frequencia_respiratoria_FR',
    #              'saturacao_de_oxigenio_SPO2', 'hemoglicoteste_HGT', 'temperatura_TEMP', 'peso', 'altura',
     #             'observacao']
      #  labels = {
       #     'observacao': 'Sintomas relatados pelo paciente',
        #}        

class TriagemEnfermariaUpdateForm(forms.ModelForm):
    class Meta:
        model = triagem
        fields = ['frequencia_cardiaca_FC', 'pressao_arterial_PA_2', 'pressao_arterial_PA', 'frequencia_respiratoria_FR',
                 'saturacao_de_oxigenio_SPO2', 'hemoglicoteste_HGT', 'temperatura_TEMP', 'peso', 'altura',
                'observacao']
    
    frequencia_cardiaca_FC = forms.FloatField(
        label='Frequência Cardíaca (FC):',
        #queryset=Pessoas.objects.none(),  # Query to fetch all Pessoas objects
        widget=forms.NumberInput(attrs={'class': ' p-1 mb-3 text-uppercase'}),
    )
    pressao_arterial_PA_2 = forms.FloatField(
        label='Pressão Arterial DIASTÓLICA:',
        #queryset=Pessoas.objects.none(),  # Query to fetch all Pessoas objects
        widget=forms.NumberInput(attrs={'class': ' p-1 mb-3 text-uppercase '}),
    )
    pressao_arterial_PA = forms.FloatField(
        label='Pressão Arterial SISTÓLICA:',
        #queryset=Pessoas.objects.none(),  # Query to fetch all Pessoas objects
        widget=forms.NumberInput(attrs={'class': ' p-1 mb-3 text-uppercase'}),
    )
    frequencia_respiratoria_FR = forms.FloatField(
        label='Frequência Respiratória (FC):',
        #queryset=Pessoas.objects.none(),  # Query to fetch all Pessoas objects
        widget=forms.NumberInput(attrs={'class': ' p-1 mb-3 text-uppercase'}),
    )
    saturacao_de_oxigenio_SPO2 = forms.FloatField(
        label='Saturação de Oxigênio (SPO²):',
        #queryset=Pessoas.objects.none(),  # Query to fetch all Pessoas objects
        widget=forms.NumberInput(attrs={'class': ' p-1 mb-3 text-uppercase'}),
    )
    hemoglicoteste_HGT = forms.FloatField(
        label='Hemoglicoteste (HGT):',
        #queryset=Pessoas.objects.none(),  # Query to fetch all Pessoas objects
        widget=forms.NumberInput(attrs={'class': ' p-1 mb-3 text-uppercase'}),
    )
    temperatura_TEMP = forms.FloatField(
        label='Temperatura (C°):',
        #queryset=Pessoas.objects.none(),  # Query to fetch all Pessoas objects
        widget=forms.NumberInput(attrs={'class': ' p-1 mb-3 text-uppercase'}),
    )
    peso = forms.FloatField(
        label='Peso (Kg):',
        #queryset=Pessoas.objects.none(),  # Query to fetch all Pessoas objects
        widget=forms.NumberInput(attrs={'class': ' p-1 mb-3 text-uppercase'}),
    )
    altura = forms.FloatField(
        label='Altura:',
        #queryset=Pessoas.objects.none(),  # Query to fetch all Pessoas objects
        widget=forms.NumberInput(attrs={'class': ' p-1 mb-3 text-uppercase'}),
    )
   
    def clean_peso(self):
        peso = self.cleaned_data.get('peso')
        if peso:
            try:
                return float(peso)
            except ValueError:
                raise forms.ValidationError("O peso deve ser um número válido.")
        return None

    def clean_altura(self):
        altura = self.cleaned_data.get('altura')
        if altura:
            try:
                return float(altura)
            except ValueError:
                raise forms.ValidationError("A altura deve ser um número válido.")
        return None

    def clean(self):
        cleaned_data = super().clean()
        peso = cleaned_data.get('peso')
        altura = cleaned_data.get('altura')

        # Adicione lógica adicional se necessário para validação combinada

        return cleaned_data

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['frequencia_cardiaca_FC'].required = True
        self.fields['pressao_arterial_PA_2'].required = True
        self.fields['pressao_arterial_PA'].required = True
        self.fields['frequencia_respiratoria_FR'].required = True
        self.fields['saturacao_de_oxigenio_SPO2'].required = True
        self.fields['hemoglicoteste_HGT'].required = True
        self.fields['temperatura_TEMP'].required = True
        self.fields['peso'].required = False
        self.fields['peso'].initial=0
        self.fields['altura'].required = False
        self.fields['altura'].initial=0
        self.fields['observacao'].required = True

        
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


    


