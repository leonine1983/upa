import calendar
from datetime import date

from Atendimento.models import envio_triagem

def registros_envio_triagem_por_mes(request):
    # Obter o ano e o mês atual
    hoje = date.today()
    ano_atual = hoje.year
    mes_atual = hoje.month

    # Obter o nome do mês atual
    nome_mes_atual = calendar.month_name[mes_atual]

    # Obter o número de dias no mês atual
    numero_dias_mes = calendar.monthrange(ano_atual, mes_atual)[1]

    # Criar a data inicial e final do mês atual
    primeira_data_mes = date(ano_atual, mes_atual, 1)
    ultima_data_mes = date(ano_atual, mes_atual, numero_dias_mes)

    # Filtrar os registros de envio_triagem pelo mês atual
    registros_por_mes = envio_triagem.objects.filter(data_envio_triagem__range=(primeira_data_mes, ultima_data_mes))

    # Contar a quantidade de registros
    quantidade_registros_por_mes = registros_por_mes.count()

    # Retornar a quantidade e o nome do mês no contexto
    return {
        'quantidade_registros_por_mes': quantidade_registros_por_mes,
        'nome_mes_atual': nome_mes_atual,
        'todos_atend': envio_triagem.objects.all().count()
    }
