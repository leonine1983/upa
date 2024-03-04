from django import forms
from Triagem.models import triagem, Exames_Model

class Form_medico_atendimento (forms.Form):

    paciente_triagem = forms.CharField(max_length=2, required=False, help_text='Nome do paciente')    
    pressao_arterial_PA = forms.CharField(help_text='Pressão arterial do paciente')
    frequencia_cardiaca_FC = forms.CharField(help_text='Frequencia Cardiaca do Paciente')
    frequencia_respiratoria_FR = forms.CharField(help_text='')
    saturacao_de_oxigenio_SPO2 = forms.CharField(help_text='')
    hemoglicoteste_HGT = forms.CharField(help_text='')
    temperatura_TEMP = forms.CharField(help_text='')
    peso = forms.CharField(help_text='')
    data_triagem = forms.CharField(help_text='')
    hora_triagem = forms.CharField(help_text='')
    classifica_tipo = forms.CharField(help_text='')
    observacao = forms.Textarea()
    final_triagem = forms.CharField(help_text='')
    final_triagem_time = forms.DateField(help_text='')


class Prescreve_Medicamentos_fomr(forms.ModelForm):
    exames = forms.ModelMultipleChoiceField(queryset=Exames_Model.objects.all(), widget=forms.SelectMultiple, required=False)

    class Meta:
        model = triagem
        fields = ['exames', 'atestado', 'preescrever_medicamento_medico']
        labels = {}
        widgets = {
            'atestado': forms.NumberInput(attrs={'type': 'range', 'min': 0, 'max': 30, 'step': 1, 'oninput': 'updateTextInput(this.value)'}),
        }

     



class ChamarPacienteForm(forms.Form):
    class Meta:
        fields = ['nome_paciente','profissionalSaude_id']
        
    nome_paciente = forms.CharField(widget=forms.HiddenInput())
    profissionalSaude_id = forms.CharField(widget=forms.HiddenInput())




       