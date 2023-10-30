from django import forms
from Atendimento.models import ficha_de_atendimento  # Importe o modelo Paciente aqui

class CadastraPacienteForm(forms.ModelForm):  # Renomeie a classe do formulário para seguir a convenção de nomenclatura do Python (CamelCase)
    class Meta:
        model = ficha_de_atendimento  # Defina o modelo do formulário
        fields = '__all__'  # Ou especifique os campos necessários separadamente

        widgets = {
            'nome_social': forms.TextInput(attrs={'class': 'form-control'}),
            'codigo_pacient':forms.TextInput(attrs={'class': 'form-control'}),
            'data_nascimento': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'YYYY-MM-DD'}),
            'sexo': forms.Select(attrs={'class': 'form-select'}),
            'RG': forms.TextInput(attrs={'class': 'form-control'}),
            'CPF': forms.TextInput(attrs={'class': 'form-control'}),
            'nacionalidade': forms.TextInput(attrs={'class': 'form-control'}),
            'rua': forms.Select(attrs={'class': 'form-select'}),
            'bairro': forms.Select(attrs={'class': 'form-select'}),
            'cidade': forms.TextInput(attrs={'class': 'form-control'}),
            'estado': forms.TextInput(attrs={'class': 'form-control'}),
            'CEP': forms.TextInput(attrs={'class': 'form-control'}),
            'nome_mae': forms.TextInput(attrs={'class': 'form-control'}),
            'responsavel': forms.TextInput(attrs={'class': 'form-control'}),
            'tel': forms.TextInput(attrs={'class': 'form-control'}),
            'cartao_sus': forms.TextInput(attrs={'class': 'form-control'}),
        }
