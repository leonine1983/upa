from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.models import Group
from django.http import  HttpResponseRedirect
from django.urls import reverse
from django.views.generic import UpdateView
#from Medicos.forms import Form_medico_atendimento
from Medicos.models import CustomUser, Medico_atendimento
from Triagem.models import triagem
from Medicos.models import CustomUser


class atendimento_medico_Atualiza(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Medico_atendimento
    #Chave Estrangeira 'paciente_medico_atendimento'
    fields = ['paciente_medico_atendimento', 'historico_doenca_atual_HDA', 'exame_fisico', 'Diagnostico', 'conduta','classificacao_internacional_doenca_CID']
    template_name = 'Medicos/medico_atendimento_atendimento.html'   
    success_message = 'Avaliação médica feita com sucesso'
     
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        pk = self.kwargs['pk']    
        trigem_id = Medico_atendimento.objects.get(pk=self.kwargs['pk'])        
        context['triagem'] = triagem.objects.filter(id = trigem_id.paciente_medico_atendimento.id)
        context['atendimento'] = 'atendimento'       

        return context
    
    #success_url = reverse_lazy('Medicos:dados do paciente_medicamentos self.kwargs['pk']')
    def get_success_url(self):
        return reverse('Medicos:dados_do_paciente_medicamentos', kwargs={'pk':self.object.paciente_medico_atendimento.id})
    
    
    















