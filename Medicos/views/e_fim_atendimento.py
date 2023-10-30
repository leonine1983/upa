from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
#Cria os usuarios
from django.urls import reverse_lazy
#restrição de acesso
from django.views.generic import DetailView, UpdateView
from Triagem.models import triagem
from Atendimento.models import *
#from Medicos.forms import Form_medico_atendimento
from Medicos.models import Medico_atendimento


class atendimento_medico_concluido_update(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = triagem
    fields = ['final_medico_atendimento']
    template_name = 'Medicos/confirma_final.html'
    success_url =reverse_lazy('Medicos:medico_prontuario')
    success_message = "Atendimento finalizado com sucesso!!"


#View que exibe o medicamento receitado pelo medico
class exibe_prescreve_medicamento_update(LoginRequiredMixin, DetailView):
    model = triagem
    template_name = 'Medicos/exibir_impressao/exibi_prescreve_medicamento.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        triagem_now = triagem.objects.filter(pk= self.kwargs['pk'])
        cid10 = Medico_atendimento.objects.filter(paciente_medico_atendimento = self.kwargs['pk'])
        #Medico_atendimento.objects.select_related('paciente_medico_atendimento__paciente_triagem__paciente_envio_triagem').filter(paciente_medico_atendimento__paciente_triagem__paciente_envio_triagem_id=paciente)
        #exames = Exames_Model.objects.filter(triagem_id = self.kwargs['pk'])
        exames = triagem.objects.select_related('triagem_exames')
      
        context = {
            'triagem_now':triagem_now,
            'cid10': cid10,
            'exames': exames
        }
        return context
        