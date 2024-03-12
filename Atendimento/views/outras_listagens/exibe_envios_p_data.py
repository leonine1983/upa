from typing import Any
from django.contrib.auth.mixins import LoginRequiredMixin
from Atendimento.models import envio_triagem
from django.views.generic.list import ListView
from datetime import datetime
from django.db.models import Count, Case, When, CharField, Value

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
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Processar a queryset para obter contagens
        pacientes_por_localidade = self.object_list.values('paciente_envio_triagem__bairro__bairro_nome').annotate(total=Count('id')).filter(paciente_envio_triagem__cidade__cidade='Vera Cruz')
        pacientes_por_cidade = self.object_list.values('paciente_envio_triagem__cidade__cidade').annotate(total=Count('id'))
        pacientes_por_sexo = self.object_list.values('paciente_envio_triagem__sexo__nome_genero').annotate(total=Count('id'))
        

        # Casos para calcular faixa etária
        cases = [
            When(paciente_envio_triagem__idade__gte=0, paciente_envio_triagem__idade__lte=1, then=Value('0 a 1 ano')),
            When(paciente_envio_triagem__idade__gte=1, paciente_envio_triagem__idade__lte=4, then=Value('1 a 4 anos')),
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
            When(paciente_envio_triagem__idade__isnull=True, then=Value('Idade não informada'))
        ]

        # Calculando pacientes por faixa etária
        pacientes_por_idade = self.object_list.annotate(
            faixa_etaria=Case(*cases, output_field=CharField())
        ).values('faixa_etaria').annotate(total=Count('id'))

        total_paciente_dia = self.object_list.count()
        data_search =self.request.GET.get('busca_data')
        if not data_search:
            data_search = datetime.today().date()
            data = data_search
        else:
            data =datetime.strptime(data_search, '%Y-%m-%d')
            data = datetime.strftime(data, '%d/%m/%Y')

        # Adicionar as contagens ao contexto
        context['data'] = data
        context['total_paciente'] = total_paciente_dia 
        context['pacientes_por_localidade'] = pacientes_por_localidade
        context['pacientes_por_idade'] = pacientes_por_idade
        context['pacientes_por_sexo'] = pacientes_por_sexo

        return context
    
   


