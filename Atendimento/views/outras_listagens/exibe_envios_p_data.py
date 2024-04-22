from typing import Any
from django.contrib.auth.mixins import LoginRequiredMixin
from Atendimento.models import envio_triagem, genero_sexual, Bairro, Cidade
from django.views.generic.list import ListView
from datetime import datetime
from django.db.models import Case, When, CharField, Value
from collections import defaultdict
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect

class Exibe_envios_data(LoginRequiredMixin, ListView):
    model = envio_triagem
    template_name = 'Atendimento/outras_listagens/envios_por_data.html'

    def get_queryset(self):
        # Data de início fornecida pela consulta GET, se não fornecida, use a data de hoje
        try:
            start_date = self.request.GET.get('busca_data', datetime.today().strftime('%Y-%m-%d'))    
            rm_classifica = self.request.GET.get('rm_classifica') 
            rm_medico = self.request.GET.get('rm_medico')   
            print(f'rm_medico : {rm_medico}')
            print(f'rm_classifica : {rm_classifica}')

            if start_date and rm_classifica and rm_medico:
                pass
            elif start_date and rm_classifica:
                object_list = envio_triagem.objects.filter(data_envio_triagem=start_date)
            elif start_date and rm_medico:
                pass
            else:
                object_list = envio_triagem.objects.filter(data_envio_triagem=start_date)  
            
            self.envios_day = object_list
            
            # Casos para calcular faixa etária
            cases = [
                When(paciente_envio_triagem__idade__gte=0, paciente_envio_triagem__idade__lte=1, then=Value('0 a 1 ano')),
                When(paciente_envio_triagem__idade__gte=2, paciente_envio_triagem__idade__lte=4, then=Value('2 a 4 anos')),
                When(paciente_envio_triagem__idade__gte=5, paciente_envio_triagem__idade__lte=9, then=Value('5 a 9 anos')),
                When(paciente_envio_triagem__idade__gte=10, paciente_envio_triagem__idade__lte=14, then=Value('10 a 14 anos')),
                When(paciente_envio_triagem__idade__gte=15, paciente_envio_triagem__idade__lte=19, then=Value('15 a 19 anos')),
                When(paciente_envio_triagem__idade__gte=20, paciente_envio_triagem__idade__lte=29, then=Value('20 a 29 anos')),
                When(paciente_envio_triagem__idade__gte=30, paciente_envio_triagem__idade__lte=39, then=Value('30 a 39 anos')),
                When(paciente_envio_triagem__idade__gte=40, paciente_envio_triagem__idade__lte=49, then=Value('40 a 49 anos')),
                When(paciente_envio_triagem__idade__gte=50, paciente_envio_triagem__idade__lte=59, then=Value('50 a 59 anos')),
                When(paciente_envio_triagem__idade__gte=60, paciente_envio_triagem__idade__lte=69, then=Value('60 a 69 anos')),
                When(paciente_envio_triagem__idade__gte=70, paciente_envio_triagem__idade__lte=79, then=Value('70 a 79 anos')),
                When(paciente_envio_triagem__idade__gte=80, paciente_envio_triagem__idade__lte=110, then=Value('80 a 110 anos')),
                When(paciente_envio_triagem__idade__gte=111, then=Value('Maior que 110')),
                When(paciente_envio_triagem__idade__isnull=True, then=Value('Idade nao informada'))
            ]        
            
            # Anotar objetos com a faixa etária correspondente
            object_list = object_list.annotate(faixa_etaria=Case(*cases, output_field=CharField()))
            return object_list
            
        except Exception as e:
            return reverse_lazy('Atendimento:listagem_envio')          

        

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Processar a queryset para obter contagens por faixa etária
        contagem_por_faixa_etaria = {
            '0 a 1': self.object_list.filter(faixa_etaria='0 a 1 ano').count(),
            '2 a 4': self.object_list.filter(faixa_etaria='2 a 4 anos').count(),
            '5 a 9': self.object_list.filter(faixa_etaria='5 a 9 anos').count(),
            '10 a 14': self.object_list.filter(faixa_etaria='10 a 14 anos').count(),
            '15 a 19': self.object_list.filter(faixa_etaria='15 a 19 anos').count(),
            '20 a 29': self.object_list.filter(faixa_etaria='20 a 29 anos').count(),
            '30 a 39': self.object_list.filter(faixa_etaria='30 a 39 anos').count(),
            '40 a 49': self.object_list.filter(faixa_etaria='40 a 49 anos').count(),
            '50 a 59': self.object_list.filter(faixa_etaria='50 a 59 anos').count(),
            '60 a 69': self.object_list.filter(faixa_etaria='60 a 69 anos').count(),
            '70 a 79': self.object_list.filter(faixa_etaria='70 a 79 anos').count(),
            '80 a 110': self.object_list.filter(faixa_etaria='80 a 110 anos').count(),
            'Maior que 110': self.object_list.filter(faixa_etaria='Maior que 110').count(),
            'Idade nao informada': self.object_list.filter(faixa_etaria='Idade nao informada').count()
        }       
        
        envios_por_genero = defaultdict(dict)
        envio_por_bairro = defaultdict(dict)
        envio_por_cidade = defaultdict(dict)

        # Contagem por Gênero
        generos_sexuais = genero_sexual.objects.all()       
        for g in generos_sexuais:
            contagem = self.envios_day.filter(paciente_envio_triagem__sexo__nome_genero=g.nome_genero).count()
            envios_por_genero[g.nome_genero] = contagem
        context['cont_genero'] = envios_por_genero.items()  
        
        # Contagem por bairro        
        bairro_nome = ['Aratuba', 'Baiacu', 'Barra do Gil', 'Barra do Pote', 'Berlinque', 'Cacha Pregos', 'Catu', 'Conceição', 'Coroa', 'Gameleira', 'Ilhota', 'Jiribatuba', 'Mar Grande', 'Ponta Grossa', 'Riachinho', 'Tairu']
        pacientes_bairro = Bairro.objects.filter(bairro_nome__in = bairro_nome)
        for b in pacientes_bairro:
            bairro_contagem = self.envios_day.filter(paciente_envio_triagem__bairro__bairro_nome = b.bairro_nome).count()
            envio_por_bairro [b.bairro_nome] = bairro_contagem    
        context['bairro_contagem'] = envio_por_bairro.items()

        # Contagem por cidade      
        pacientes_cidade = Cidade.objects.all()
        for c in pacientes_cidade:
            cidade_contagem = self.envios_day.filter(paciente_envio_triagem__cidade__cidade = c.cidade).count()
            envio_por_cidade [c.cidade] = cidade_contagem   
        context['cidade_contagem'] = envio_por_cidade.items()

        total_paciente_dia = self.object_list.count()
        data_search = self.request.GET.get('busca_data', datetime.today().strftime('%Y-%m-%d'))
        data = datetime.strptime(str(data_search), '%Y-%m-%d').strftime('%d/%m/%Y')

        # Adicionar as contagens ao contexto
        context['data'] = data
        context['total_paciente'] = total_paciente_dia 
        context['contagem_por_faixa_etaria'] = contagem_por_faixa_etaria

        return context

