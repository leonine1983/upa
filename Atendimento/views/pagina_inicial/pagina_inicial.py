from datetime import datetime, timedelta
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from django.db.models import Count
from Atendimento.models import envio_triagem

from dateutil.relativedelta import relativedelta

import io
import base64
#import matplotlib.pyplot as plt
#from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas


@login_required
def pagina_inicial(request):
    data = datetime.today() 
    data_ontem = datetime.now() - timedelta(days=1)
    paciente_ontem = envio_triagem.objects.filter(triagem_concluida = 1) & envio_triagem.objects.filter(data_triagem_concluida = data_ontem)  
    pacient_localidade_ontem = paciente_ontem.values('paciente_envio_triagem__bairro__bairro_nome').annotate(Total = Count('paciente_envio_triagem__bairro') )
    paciente_dia = envio_triagem.objects.filter(triagem_concluida = 1) & envio_triagem.objects.filter(data_triagem_concluida = data)  
    pacient_localidade = paciente_dia.values('paciente_envio_triagem__bairro__bairro_nome').annotate(Total = Count('paciente_envio_triagem__bairro') )
    h = "Masculino"
    m = "Feminino"
   
    # Extraia os dados de localidades do contexto Django
    localidades = []
    quantidades = []
    for item in pacient_localidade:
        localidades.append(item['paciente_envio_triagem__bairro__bairro_nome'])
        quantidades.append(item['Total'])
    """
    # Gere o gráfico
    fig, ax = plt.subplots()
    ax.bar(localidades, quantidades)
    ax.set_xlabel('Localidades')
    ax.set_ylabel('Número de Atendimentos')
    ax.set_title('Atendimentos por Localidade')
    
    # Salve a imagem em um buffer
    buffer = io.BytesIO()
    FigureCanvas(fig).print_png(buffer)
    buffer.seek(0)

    # Converta a imagem para base64 para incluí-la no contexto do Django
    imagem_base64 = base64.b64encode(buffer.read()).decode('utf-8')
    
    
    
    
    
    
    
    
    """
    import calendar


    # Obter o ano e o mes
    ano_atual = datetime.today().year
    mes_atual = datetime.today().month

    # Obter todos os dias do mês atual
    _, num_dias = calendar.monthrange(ano_atual, mes_atual)
    dias_do_mes = [datetime(ano_atual, mes_atual, dia) for dia in range(1, num_dias + 1)]

    resultados_por_dia = {}  # Dicionário para armazenar os resultados por dia

    for d in dias_do_mes:
        object_list = envio_triagem.objects.filter(data_envio_triagem=d, triagem_concluida=1)
        dia = d.day
        resultados_por_dia[dia] = object_list

    # Renderize a página
    return render(request, 'Atendimento/pagina_inicial.html', {
        'resultados_por_dia': resultados_por_dia,
        'ano_atual': ano_atual,
        'mes_atual': mes_atual,
    })