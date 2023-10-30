from django import forms
from django.contrib.auth.models import User
from Triagem.models import Atendimento_especializado
from Triagem.models import triagem




class Atend_especializado_UpdateView_Form(forms.ModelForm):

    class Meta:
        model = Atendimento_especializado
        fields = ['situacao', 'tipo_atendimento', 'descreve_solicitacao', 'nome_medico', 'pk_paciente']
        widgets = {
           #'pk_paciente': forms.HiddenInput(),
            'tipo_atendimento': forms.TextInput(attrs={'disabled': 'disabled'}),
            'descreve_solicitacao': forms.Textarea(attrs={'disabled': 'disabled'}),
            'nome_medico': forms.TextInput(attrs={'disabled': 'disabled'}),
            
            'pk_paciente': forms.Select(attrs={'disabled': 'disabled'}),
        }

    def __init__(self, *args, **kwargs):
        request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)
        if request and request.user.is_authenticated:
            self.fields['nome_medico'].initial = request.user.username


    def clean(self):
        cleaned_data = super().clean()
        # Aqui você pode adicionar validações adicionais se necessário
        return cleaned_data
