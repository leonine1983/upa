from Triagem.models import Atendimento_especializado
from django.views.generic import CreateView
from .atend_especializado_Form import *
from Triagem.models import triagem
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404


class Atend_especializado_Create(CreateView):
    model = Atendimento_especializado
    form_class = Atend_especializado_Form
    template_name = 'Triagem/atend_especializado_listView.html'
    success_url = reverse_lazy('Medicos:medico_prontuario')

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        pk = self.request.GET.get("param")
        contexto['pk'] = pk
        paciente_triagem = get_object_or_404(triagem, id=pk).paciente_triagem
        contexto['pk_nome'] = paciente_triagem

        # Inicializa o campo 'pk_paciente' no formulário
        form = self.get_form()
        form.fields['pk_paciente'].queryset = triagem.objects.filter(pk=pk)
        form.fields['pk_paciente'].initial = triagem.objects.filter(pk=pk).first()
        contexto['form'] = form

        return contexto
