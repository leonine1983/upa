from django import forms
from django.contrib.auth.models import User
from Triagem.models import Atendimento_especializado

class Atend_especializado_Form(forms.ModelForm):
    class Meta:
        model = Atendimento_especializado
        fields = ['tipo_atendimento', 'descreve_solicitacao', 'nome_medico', 'pk_paciente']
        widgets = {
           #'pk_paciente': forms.HiddenInput(),
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
