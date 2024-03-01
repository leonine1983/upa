from django import forms
from Atendimento.models import ficha_de_atendimento  # Importe o modelo Paciente aqui

class CadastraPacienteForm(forms.ModelForm):  # Renomeie a classe do formulário para seguir a convenção de nomenclatura do Python (CamelCase)
    class Meta:
        model = ficha_de_atendimento  # Defina o modelo do formulário
        fields = '__all__'  # Ou especifique os campos necessários separadamente

        widgets = {
            'nome_social': forms.TextInput(attrs={'class': 'form-control text-uppercase bg-primary fs-1'}),
            'codigo_pacient':forms.TextInput(attrs={'class': 'form-control'}),
            'data_nascimento': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'DD/MM/AAAA'}),
            'sexo': forms.Select(attrs={'class': 'form-select text-uppercase'}),
            'RG': forms.TextInput(attrs={'class': 'form-control '}),
            'CPF': forms.TextInput(attrs={'class': 'form-control'}),
            'nacionalidade': forms.TextInput(attrs={'class': 'form-control text-uppercase'}),
            'rua': forms.TextInput(attrs={'class': 'form-control text-uppercase bg-primary'}),
            'bairro': forms.Select(attrs={'class': 'form-select text-uppercase'}),
            'cidade': forms.TextInput(attrs={'class': 'form-control text-uppercase'}),
            'estado': forms.TextInput(attrs={'class': 'form-control text-uppercase'}),
            'CEP': forms.TextInput(attrs={'class': 'form-control text-uppercase'}),
            'nome_mae': forms.TextInput(attrs={'class': 'form-control text-uppercase'}),
            'responsavel': forms.TextInput(attrs={'class': 'form-control text-uppercase'}),
            'tel': forms.TextInput(attrs={'class': 'form-control text-uppercase'}),
            'cartao_sus': forms.TextInput(attrs={'class': 'form-control '}),
        }
