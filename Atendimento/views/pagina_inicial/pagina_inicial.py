from datetime import datetime, timedelta
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from django.db.models import Count
from Atendimento.models import envio_triagem, ficha_de_atendimento

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import io
import base64

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import io
import base64


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
    
    # Renderize a página
    return render(request, 'Atendimento/pagina_inicial.html', {
        'imagem_base64': imagem_base64,
        'quant' : int(len(ficha_de_atendimento.objects.all())),
        'quant_homem' : len(ficha_de_atendimento.objects.filter(sexo = 1)),
        'quant_mulher' : len(ficha_de_atendimento.objects.filter(sexo = 2)),
        'nome_sistema' : "SG-UPA Sistema de Gerenciamento de Pronto Atendimento",
        'nome_estabelecimento': 'UPA',
        'quant_atendimentos_diario': len(envio_triagem.objects.filter(triagem_concluida = 1) & envio_triagem.objects.filter(data_triagem_concluida = data)),
        
        'quant_atendimentos_diario_H': len(envio_triagem.objects.filter(triagem_concluida = 1) & envio_triagem.objects.filter(data_triagem_concluida = data) & envio_triagem.objects.filter(paciente_envio_triagem__sexo__nome_genero = h)),         
        'quant_H_idosos': len(envio_triagem.objects.filter(triagem_concluida = 1) & envio_triagem.objects.filter(data_triagem_concluida = data) & envio_triagem.objects.filter(paciente_envio_triagem__sexo__nome_genero = h) & envio_triagem.objects.filter(paciente_envio_triagem__idade__gte=60, paciente_envio_triagem__idade__lte=130)),
        'quant_H_adultos': len(envio_triagem.objects.filter(triagem_concluida = 1) & envio_triagem.objects.filter(data_triagem_concluida = data) & envio_triagem.objects.filter(paciente_envio_triagem__sexo__nome_genero = h) & envio_triagem.objects.filter(paciente_envio_triagem__idade__gte=18, paciente_envio_triagem__idade__lte=59.99)), 
        'quant_H_adolescentes': len(envio_triagem.objects.filter(triagem_concluida = 1) & envio_triagem.objects.filter(data_triagem_concluida = data) & envio_triagem.objects.filter(paciente_envio_triagem__sexo__nome_genero = h) & envio_triagem.objects.filter(paciente_envio_triagem__idade__gte=12, paciente_envio_triagem__idade__lte=17.9)), 
        'quant_H_criancas': len(envio_triagem.objects.filter(triagem_concluida = 1) & envio_triagem.objects.filter(data_triagem_concluida = data) & envio_triagem.objects.filter(paciente_envio_triagem__sexo__nome_genero = h) & envio_triagem.objects.filter(paciente_envio_triagem__idade__gte=1, paciente_envio_triagem__idade__lte=11.9)), 
        'quant_H_bebe': len(envio_triagem.objects.filter(triagem_concluida = 1) & envio_triagem.objects.filter(data_triagem_concluida = data) & envio_triagem.objects.filter(paciente_envio_triagem__sexo__nome_genero = h) & envio_triagem.objects.filter(paciente_envio_triagem__idade=0)), 
        #'quant_H_adultos': len(envio_triagem.objects.filter(triagem_concluida = 1) & envio_triagem.objects.filter(data_triagem_concluida = data) & envio_triagem.objects.filter(paciente_envio_triagem__sexo = 1) & envio_triagem.objects.filter(paciente_envio_triagem__sexo = 1) ),
        'quant_atendimentos_diario_F': len(envio_triagem.objects.filter(triagem_concluida = 1) & envio_triagem.objects.filter(data_triagem_concluida = data) & envio_triagem.objects.filter(paciente_envio_triagem__sexo__nome_genero = m)),        
        'quant_F_idosos': len(envio_triagem.objects.filter(triagem_concluida = 1) & envio_triagem.objects.filter(data_triagem_concluida = data) & envio_triagem.objects.filter(paciente_envio_triagem__sexo__nome_genero = m) & envio_triagem.objects.filter(paciente_envio_triagem__idade__gte=60, paciente_envio_triagem__idade__lte=130)),
        'quant_F_adultos': len(envio_triagem.objects.filter(triagem_concluida = 1) & envio_triagem.objects.filter(data_triagem_concluida = data) & envio_triagem.objects.filter(paciente_envio_triagem__sexo__nome_genero = m) & envio_triagem.objects.filter(paciente_envio_triagem__idade__gte=18, paciente_envio_triagem__idade__lte=59.99)), 
        'quant_F_criancas': len(envio_triagem.objects.filter(triagem_concluida = 1) & envio_triagem.objects.filter(data_triagem_concluida = data) & envio_triagem.objects.filter(paciente_envio_triagem__sexo__nome_genero = m) & envio_triagem.objects.filter(paciente_envio_triagem__idade__gte=1, paciente_envio_triagem__idade__lte=12)), 
        'quant_F_bebe': len(envio_triagem.objects.filter(triagem_concluida = 1) & envio_triagem.objects.filter(data_triagem_concluida = data) & envio_triagem.objects.filter(paciente_envio_triagem__sexo__nome_genero = m ) & envio_triagem.objects.filter(paciente_envio_triagem__idade=0)), 
      
        'qquant_localidades': envio_triagem.objects.values('paciente_envio_triagem__bairro').annotate(total=Count('paciente_envio_triagem__bairro')),
        'quant_localidades': pacient_localidade,
        'ontem'    : paciente_ontem,
        'ontem_quantidade' : pacient_localidade_ontem
        
    })