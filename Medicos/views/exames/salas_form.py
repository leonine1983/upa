from django import forms
from Medicos.models import CadastroSala

# widget personalizado que usa as classes (form-control, border, p-3, pb-3 e bg-transparent) para ser atribuido ao campo 'tempo_meses' 


class Salas_form (forms.ModelForm):   
    
    class Meta:
        model = CadastroSala
        fields = '__all__'     
    
    nome_Sala = forms.CharField(
        label='Nome da nova sala de atendimento:',
        widget=forms.TextInput(attrs={'class': ' border border-info p-1 pb-1 bg-transparent text-info m-2 rounded-1 w-75'}),
        initial='Ex: Sala de pediatria'
    )   
    descricao_Sala = forms.CharField(
        label='Descreva a finalidade da nova sala:',
        widget=forms.Textarea(attrs={'class': ' border border-info p-3 pb-1 bg-transparent text-info m-2 rounded-1 w-75'}),
        initial= 'Ex.: Sala de atendimento pediátrico'
    )  


