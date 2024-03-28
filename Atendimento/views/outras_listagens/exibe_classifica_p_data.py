from typing import Any
from django.contrib.auth.mixins import LoginRequiredMixin
from Atendimento.models import envio_triagem
from Triagem.models import triagem
from Medicos.models import Medico_atendimento
from django.views.generic.list import ListView
from datetime import datetime
from django.db.models import Count, Case, When, CharField, Value

class Exibe_envios_data_atendimentos(LoginRequiredMixin, ListView):
    model = Medico_atendimento
    template_name = template_name = 'Atendimento/outras_listagens/envios_por_data_classifica.html'

    # pesquisa por data
    def get_queryset(self):
        start_date = self.request.GET.get('busca_data')
        date_today = datetime.today()
        #converte o formato da data
        date_hoje = '{}-{}-{}'.format(date_today.year, date_today.month, date_today.day)

        
        
        if start_date:
            #converte a str objects em date
            date = datetime.strptime(start_date, '%Y-%m-%d')        
            
            #converte o formato da data
            date_format = '{}-{}-{}'.format(date.year, date.month, date.day)
            
            if date_format:
                object_list = Medico_atendimento.objects.filter(data_medico = date_format) & Medico_atendimento.objects.filter(paciente_medico_atendimento__final_medico_atendimento = 1)
            else:             
                object_list = Medico_atendimento.objects.all() & Medico_atendimento.objects.exclude(paciente_medico_atendimento__final_medico_atendimento = 1)
        else:
            object_list = Medico_atendimento.objects.filter(data_medico = date_hoje) & Medico_atendimento.objects.exclude(paciente_medico_atendimento__final_medico_atendimento = 1)

        return object_list
    
    
   


