#Restringir acesso
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import UpdateView

from Atendimento.models import envio_triagem, ficha_de_atendimento
from Triagem.models import triagem
from Triagem.forms import TriagemEnfermaria_Alergias_UpdateForm
from django.db.models import Max

        
# verificar se o paciente possui alergia e depois envia para classificação de risco
class triagem_enfermaria_Alergia_Update(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = ficha_de_atendimento
    form_class = TriagemEnfermaria_Alergias_UpdateForm
    template_name = 'Triagem/triagem.html'
    success_message = "Alergia cadastrada ao paciente com sucesso!"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['triagem_andamento'] = "ok" 
        context ['nome_paciente'] = self.object.nome_social        
        context ['tipo_titulo'] = 'Pré-atendimento | ALERGIAS e COMORBIDADES'
        context ['tipo_select'] = f"{self.kwargs['pk']} - {envio_triagem.objects.filter(paciente_envio_triagem_id=self.kwargs['pk']).aggregate(Max('id'))['id__max']}"
        return context

    def get_success_url(self):
        # Busca o último lançamento do paciente no envio_triagem
        ultimo_envio_triagem_id = envio_triagem.objects.filter(paciente_envio_triagem_id=self.kwargs['pk']).aggregate(Max('id'))['id__max']
        
        if ultimo_envio_triagem_id:
            # Busca o ID correspondente na tabela triagem
            classifica_risco_id = triagem.objects.filter(paciente_triagem__id=ultimo_envio_triagem_id).values_list('id', flat=True).first()
            print(classifica_risco_id)
            
            return reverse('Triagem:triagem_classifica_Risco_update', kwargs={'pk': classifica_risco_id})

        # Caso não encontre nenhum ID correspondente, retorna a URL padrão
        return super().get_success_url()
    
