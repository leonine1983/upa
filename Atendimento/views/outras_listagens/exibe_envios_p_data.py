from typing import Any
from django.contrib.auth.mixins import LoginRequiredMixin
from Atendimento.models import envio_triagem
from django.views.generic.list import ListView
from datetime import datetime

class Exibe_envios_data(LoginRequiredMixin, ListView):
    model = envio_triagem
    template_name = template_name = 'Atendimento/outras_listagens/envios_por_data.html'

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

            print(date_format)  
            
            if date_format:
                object_list = envio_triagem.objects.filter(data_envio_triagem = date_format) 
            else:             
                object_list = envio_triagem.objects.all() & envio_triagem.objects.exclude(triagem_concluida = 1)
        else:
            object_list = envio_triagem.objects.filter(data_envio_triagem = date_hoje) & envio_triagem.objects.exclude(triagem_concluida = 1)

        return object_list
    
   


