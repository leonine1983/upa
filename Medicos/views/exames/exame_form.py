from django import forms
from Triagem.models import Exames_Model

# widget personalizado que usa as classes (form-control, border, p-3, pb-3 e bg-transparent) para ser atribuido ao campo 'tempo_meses' 


class Exame_form (forms.ModelForm):   
    
    class Meta:
        model = Exames_Model
        fields = '__all__'     
    
    nome_exame = forms.CharField(
        label='Nome do novo exame:',
        widget=forms.TextInput(attrs={'class': ' border border-info p-1 pb-1 bg-transparent text-info m-2 rounded-1 w-75'}),
        initial='Ex: Exame de sangue'
    )   
    

class Exame_form_update (forms.ModelForm):   
    
    class Meta:
        model = Exames_Model
        fields = '__all__'     
    
    nome_exame = forms.CharField(
        label='Exame a ser atualizado:',
        widget=forms.TextInput(attrs={'class': ' border border-info p-1 pb-1 bg-transparent text-info m-2 rounded-1 w-75'}),
    )  
    

