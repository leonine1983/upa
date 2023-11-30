from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import  UpdateView
from Triagem.models import triagem
from Medicos.models import Medico_atendimento
from Atendimento.models import *
from Triagem.models import triagem
from django.contrib.auth.mixins import LoginRequiredMixin


# -------------------------- PREESCRIÇÃO DE EXAMES, MEDICAMENTOS, ATESTADOS ---------------------------------------------------------
class atendimento_medico_updateview(LoginRequiredMixin, UpdateView):
    model = triagem 
    fields = ['preescrever_medicamento_medico', 'exames', 'atestado']   
    template_name = 'Medicos/prescrever-medicamento.html'
    
    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto['pk'] = self.kwargs['pk']
        contexto['resultado_medico'] = Medico_atendimento.objects.filter(paciente_medico_atendimento_id = self.kwargs['pk'])
        return contexto

    def get_success_url(self):
        envio_filter = self.kwargs['pk']
        triagem_filter = triagem.objects.filter(id = envio_filter)
        for n in triagem_filter:
            key = n.id
            data_key = n.data_triagem   

        return reverse('Medicos:exibe_prescreve_medicamento', kwargs={'pk':key})     
        