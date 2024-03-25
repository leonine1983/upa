from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView
from Triagem.models import triagem
from Atendimento.models import *
from Medicos.models import Medico_atendimento
from Medicos.forms import Prescreve_Medicamentos_fomr


class atendimento_medico_concluido_update(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = triagem
    fields = ['final_medico_atendimento']
    template_name = 'Medicos/confirma_final.html'
    success_url =reverse_lazy('Medicos:medico_prontuario')
    success_message = "Atendimento finalizado com sucesso!!"



class exibe_prescreve_medicamento_update(LoginRequiredMixin, UpdateView):

    model = triagem
    success_message = "Impressão do documentos atualizados com sucesso!!"
    template_name = 'Medicos/exibir_impressao/exibi_prescreve_medicamento.html'
    form_class = Prescreve_Medicamentos_fomr

    def get_success_url(self):
        return reverse_lazy("Medicos:exibe_prescreve_medicamento", kwargs={'pk': self.object.pk})

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Recuperar a instância única de triagem
        triagem_instance = triagem.objects.get(pk=self.kwargs['pk'])
        
        # Outras consultas para recuperar informações adicionais
        cid10 = Medico_atendimento.objects.filter(paciente_medico_atendimento=self.kwargs['pk'])
        exames = triagem_instance.exames.all()

        # Atualizar o contexto existente com as novas variáveis
        context.update({
            'triagem_now': triagem_instance,
            'cid10': cid10,
            'exames': exames,
        })

        return context
        