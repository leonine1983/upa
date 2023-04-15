from django import forms

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