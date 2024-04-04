from typing import Any
from django.contrib.auth.mixins import LoginRequiredMixin
from Atendimento.models import envio_triagem
from Triagem.models import triagem
from Medicos.models import Medico_atendimento
from django.views.generic.list import ListView
from datetime import datetime
from django.db.models import Count, Case, When, CharField, Value

class Exibe_documentos_paciente(LoginRequiredMixin, ListView):
    model = envio_triagem
    template_name = template_name = 'Atendimento/outras_listagens/envios_documento_paciente.html'

    # pesquisa por data
    def get_queryset(self):
        start_busca_paciente = self.request.GET.get('busca_paciente')
        start_date = self.request.GET.get('busca_data')
        date_today = datetime.today()
        #converte o formato da data
        date_hoje = '{}-{}-{}'.format(date_today.year, date_today.month, date_today.day)
        
        if start_busca_paciente:
            #converte a str objects em date
            date = datetime.strptime(start_date, '%Y-%m-%d')    
            #converte o formato da data
            date_format = '{}-{}-{}'.format(date.year, date.month, date.day)

            print(date_format)  
            self.object_list = envio_triagem.objects.filter(paciente_envio_triagem__nome_social__icontains = start_busca_paciente, data_envio_triagem=date_format) 
            self.object_triagem = triagem.objects.filter(paciente_triagem__paciente_envio_triagem__nome_social__icontains = start_busca_paciente, data_envio_a_classificao=date_format)
            self.object_medic_atendimento = Medico_atendimento.objects.filter(paciente_medico_atendimento__paciente_triagem__paciente_envio_triagem__nome_social__icontains = start_busca_paciente, data_medico=date_format)
        else:
            self.object_list = envio_triagem.objects.filter(data_envio_triagem = datetime.today())
            self.object_triagem  = triagem.objects.filter(data_triagem = datetime.today())
            self.object_medic_atendimento  = Medico_atendimento.objects.filter(data_medico = datetime.today())

        return self.object_list

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)        
        context['object_list'] = self.object_list,
        context['object_triagem'] = self.object_triagem,
        context['object_medic_atendimento'] = self.object_medic_atendimento

        return context
    
   


