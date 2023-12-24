#Restringir acesso
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import UpdateView

from Atendimento.models import envio_triagem, ficha_de_atendimento
from Triagem.models import triagem
from Triagem.forms import TriagemEnfermaria_Alergias_UpdateForm
from django.db.models import Max
from django.http import Http404
from datetime import datetime

        
# verificar se o paciente possui alergia e depois envia para classificação de risco
class triagem_enfermaria_Alergia_Update(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = ficha_de_atendimento
    form_class = TriagemEnfermaria_Alergias_UpdateForm
    template_name = 'Triagem/triagem.html'
    success_message = "Alergia cadastrada ao paciente com sucesso!"


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['nome_paciente'] = self.object.nome_social        
        context ['tipo_titulo'] = 'Pré-atendimento | ALERGIAS e COMORBIDADES'
        context ['tipo_select'] = f"{self.kwargs['pk']} - {envio_triagem.objects.filter(paciente_envio_triagem_id=self.kwargs['pk']).aggregate(Max('id'))['id__max']}"
        return context
    
    def get(self, request, *args, **kwargs):
        self.hora = kwargs.get('hora')
        self.data = kwargs.get('data')
        self.paciente_envio_triagem_id = kwargs.get('paciente_envio_triagem_id')

        return super().get(request, hora=self.hora, data=self.data, paciente_envio_triagem_id=self.paciente_envio_triagem_id)

    def get_success_url(self, **kwargs):
        # Obtém os valores dos parâmetros da URL
        hora = self.kwargs.get('hora')
        data = self.kwargs.get('data')
        print(hora)
        print(f'Primeira data {data}')
        data = datetime.strptime(data, '%Y-%m-%d').date()
        print(f'segunda data {data}')
      
        pk_fila= self.kwargs.get('paciente_envio_triagem_id')
        print(f'pk enviado pela url {pk_fila}')

        

        classifica_risco_id = triagem.objects.get(
                    id=pk_fila,
                    data_envio_a_classificao=data,
                    #hora_envio_a_classificao=hora
                ).id
        print(f'pk classifica riscok, triagm {classifica_risco_id}')
        
        return reverse('Triagem:triagem_classifica_Risco_update', kwargs={'pk': classifica_risco_id})