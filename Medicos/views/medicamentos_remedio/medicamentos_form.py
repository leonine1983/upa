from django import forms
from Medicos.models import Medicamento

# widget personalizado que usa as classes (form-control, border, p-3, pb-3 e bg-transparent) para ser atribuido ao campo 'tempo_meses' 


class Medicamento_form (forms.ModelForm):   
    
    class Meta:
        model = Medicamento
        fields = '__all__'     
    
    nome_medicamento = forms.CharField(
        label='Nome do Medicamento:',
        widget=forms.TextInput(attrs={'class': ' border border-info p-1 pb-1 bg-transparent text-info m-2 rounded-1 w-75'}),
      
    )   
    principio_ativo = forms.CharField(
        label='Princípio Ativo:',
        widget=forms.TextInput(attrs={'class': ' border border-info p-1 pb-1 bg-transparent text-info m-2 rounded-1 w-75'}),
      
    )  
    forma_farmaceutica = forms.CharField(
        label='Fórmula Famaceutica:',
        widget=forms.TextInput(attrs={'class': ' border border-info p-1 pb-1 bg-transparent text-info m-2 rounded-1 w-75'}),
      
    )  
    concentracao = forms.CharField(
        label='Concentração:',
        widget=forms.TextInput(attrs={'class': ' border border-info p-1 pb-1 bg-transparent text-info m-2 rounded-1 w-75'}),
       
    ) 
    via_administracao = forms.CharField(
        label='Via de administração:',
        widget=forms.TextInput(attrs={'class': ' border border-info p-1 pb-1 bg-transparent text-info m-2 rounded-1 w-75'}),
        
    ) 
    quantidade_disponivel = forms.CharField(
        label='Quantidade Disponível:',
        widget=forms.TextInput(attrs={'class': ' border border-info p-1 pb-1 bg-transparent text-info m-2 rounded-1 w-75'}),
       
    ) 
    unidade_medida = forms.CharField(
        label='Unidade de Medida:',
        widget=forms.TextInput(attrs={'class': ' border border-info p-1 pb-1 bg-transparent text-info m-2 rounded-1 w-75'}),
        initial='Ex: kg'
    ) 
    data_validade = forms.DateField(
        label='Data de Validade:',
        widget=forms.DateInput(attrs={'class': ' border border-info p-3 pb-1 bg-transparent text-info m-2 rounded-1 w-75'}),
        
    ) 
    fabricante = forms.CharField(
        label='Fabricante:',
        widget=forms.TextInput(attrs={'class': ' border border-info p-1 pb-1 bg-transparent text-info m-2 rounded-1 w-75'}),
        
    ) 
    observacoes = forms.CharField(
        label='Observação sobre o medicamento:',
        widget=forms.Textarea(attrs={'class': ' border border-info p-3 pb-1 bg-transparent text-info m-2 rounded-1 w-75'}),
        
    ) 
